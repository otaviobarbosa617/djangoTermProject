from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView
from .models import Book, InstanceBook, Author, BookGenre, Language, Cart


def home(request):
    session_id = request.session.get('session_id', 0)
    request.session['session_id'] = session_id + 1
    context = {
        'session_id': session_id
    }
    return render(request, 'home.html', context=context)


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
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'


class BookByGenreListView(generic.DetailView):
    model = BookGenre
    template_name = 'books_by_genre.html'


class CartListView(generic.ListView):
    model = Cart
    context_object_name = 'cart_list'
    template_name = 'cart.html'

# This is for a future separation between admin and a regular user.
# For now, if you want to add book, you can add through admin page
# class BookCreate(CreateView):
#     model = Book
#     fields = ['book_isbn', 'book_name', 'book_author', 'book_genre', 'book_language', 'book_launch_year',
#               'book_acquired_year', 'book_description', 'book_quantity']
#     template_name = 'book_form.html'
