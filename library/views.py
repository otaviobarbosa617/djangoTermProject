from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView
from .models import Book, InstanceBook


def home(request):
    return render(request, 'home.html')


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


class BookCreate(CreateView):
    model = Book
    fields = ['book_isbn', 'book_name', 'book_author', 'book_genre', 'book_language', 'book_launch_year',
              'book_acquired_year', 'book_description', 'book_quantity']
    template_name = 'book_form.html'
