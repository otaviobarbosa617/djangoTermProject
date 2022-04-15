from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookForm
from .models import Book, BookGenre, Author, InstanceBook
from django.views import generic


def home(request):
    return render(request, 'home.html')


def add_book(request):
    return render(request, 'addbook.html')


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


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    queryset = Book.objects.all()
    template_name = 'books.html'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'


class FormAddView(generic.FormView):
    template_name = 'addbook.html'
    form_class = BookForm
