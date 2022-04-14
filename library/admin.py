from django.contrib import admin
from .models import Author, BookGenre, Book, InstanceBook, Language

# Register your models here.

admin.site.register(BookGenre)
admin.site.register(Language)


class BooksInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'author_last_name',
        'author_first_name'
    )
    fields = ['author_last_name', 'author_first_name']
    inlines = [BooksInline]


admin.site.register(Book)
admin.site.register(InstanceBook)