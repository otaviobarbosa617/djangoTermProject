import datetime
from django.db import models
from django.core.validators import MinValueValidator, validate_comma_separated_integer_list
from django.db.models import DO_NOTHING


class BookGenre(models.Model):
    GENRE_CHOICES = (
        (None, 'Select a Genre:'),
        ('FY', 'Fantasy'),
        ('ACT', 'Action'),
        ('ADV', 'Adventure'),
        ('CLA', 'Classics'),
        ('MYS', 'Mystery'),
        ('HIF', 'Historical Fiction'),
        ('HOR', 'Horror'),
        ('NOV', 'Novel'),
        ('ROM', 'Romance'),
        ('SCF', 'Sci-fi'),
        ('EDC', 'Educational'),
        ('SCI', 'Science'),
        ('BIO', 'Biography'),
        ('SHO', 'Short Stories'),
        ('SUS', 'Suspense'),
        ('COK', 'Cookbook'),
        ('HIS', 'History'),
        ('POE', 'Poetry'),
        ('SEL', 'Self-help'),
        ('TRC', 'True crime'),
        ('CHI', 'Children'),
        ('GRA', 'Graphic-Novel & Comic Book'),
        ('ART', 'Art & Photography'),
        ('TRA', 'Travel & Vacation'),
        ('HUM', 'Humor'),
        ('GUI', 'Guide & How-To'),
        ('REL', 'Religion & Spirituality'),
        ('HUS', 'Humanities & Social Sciences'),
        ('PAR', 'Parenting'),
        ('TEC', 'Technology'),
        ('NON', 'Non-Fiction'),
        ('DRA', 'Drama')
    )
    item_genre = models.CharField(max_length=3, choices=GENRE_CHOICES)


class Book(models.Model):
    book_sku = models.IntegerField('SKU')
    book_launch_year = models.DateTimeField('Date Published')
    book_acquired_year = models.DateTimeField('Acquisition Date')
    book_name = models.CharField('Name', max_length=200, unique_for_date=book_launch_year)
    book_author_input = models.CharField(max_length=200, validators=[validate_comma_separated_integer_list])
    book_genre = models.ManyToManyField(BookGenre, choices=BookGenre.GENRE_CHOICES)
    book_quantity = models.IntegerField('Quantity')
    book_quantity_available = models.IntegerField('Amount available')


class BookAuthor(models.Model):
    book_author = models.ManyToManyField(Book)
