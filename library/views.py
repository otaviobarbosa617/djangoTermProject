from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookForm
from .models import Book, BookGenre, Author, InstanceBook


def home(request):
    return render(request, 'base.html')


def add_book(request):
    return render(request, 'addbook.html')

def view_all_books(request):
    books = Book.objects.all()
    context = {
        'book_list': books
    }
    return render(request,'booksall.html', context=context)