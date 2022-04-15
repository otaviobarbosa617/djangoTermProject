from datetime import date
import uuid
from django.db import models
from django.core.validators import MinValueValidator, validate_comma_separated_integer_list
from django.db.models import DO_NOTHING
from django.urls import reverse
from django.contrib.auth.models import User


class Language(models.Model):
    language_name = models.CharField(max_length=50)

    def __str__(self):
        return self.language_name


class BookGenre(models.Model):
    item_genre = models.CharField(max_length=20)

    def __str__(self):
        return self.item_genre


class Author(models.Model):
    author_first_name = models.CharField(max_length=120)
    author_last_name = models.CharField(max_length=120)

    class Meta:
        ordering = ['author_last_name', 'author_first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.author_last_name.capitalize()}, {self.author_first_name}'


class Book(models.Model):
    book_isbn = models.CharField('ISBN', max_length=13, unique=True, default=0)
    book_name = models.CharField('Name', max_length=200)
    # AFTER finishing, I noticed that this is a logical error: A book can have multiple authors
    book_author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    book_genre = models.ManyToManyField(BookGenre, blank=True)
    book_language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    book_launch_year = models.DateField('Date Published')
    book_acquired_year = models.DateField('Acquisition Date')
    book_description = models.TextField(max_length=1000, null=True, blank=True)
    book_quantity = models.IntegerField('Quantity')

    class Meta:
        ordering = ['book_name']

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join([genre.name for genre in self.book_genre.all()[:3]])

    display_genre.short_description = 'Genre'

    def short_description(self):
        short_description_len = 200
        if len(self.book_description) > short_description_len:
            new_short_desc = self.book_description[:short_description_len] + '...'
            return new_short_desc
        else:
            return self.book_description

class InstanceBook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    book_due_date = models.DateField(null=True, blank=True)
    book_borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    BOOK_STATUS_CHOICES = (
        ('ava', 'Available'),
        ('onl', 'Loaned'),
        ('una', 'Unavailable')
    )

    book_status = models.CharField(max_length=3, choices=BOOK_STATUS_CHOICES,
                                   blank=True, default='ava', help_text='Book Availability')

    @property
    def is_overdue(self):
        if self.book_due_date and date.today() > self.book_due_date:
            return True
        return False

    class Meta:
        ordering = ['book_due_date']

    def __str__(self):
        return f'{self.id} ({self.book.book_name})'
