from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookForm
from .models import Book, BookGenre, Author, InstanceBook


def home(request):
    return render(request, 'home.html')


def add_book(request):
    return render(request, 'addbook.html')

def view_all_books(request):
    books = Book.objects.all()
    context = {
        'book_list': books
    }
    return render(request,'booksall.html', context=context)

def library_stats(request):
    num_books = Book.objects.all().count()
    available_books = InstanceBook.objects.filter(book__instancebook__book_status__iexact='ava').count()
    loaned_books = InstanceBook.objects.filter(book__instancebook__book_status__iexact='onl').count()
    context = {
        'num_books': num_books,
        'ava_books': available_books,
        'lon_books': loaned_books
    }

    return render(request, 'librarystats.html', context=context)