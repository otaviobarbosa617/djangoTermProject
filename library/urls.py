from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    # path('book/add_book/', views.BookCreate.as_view(), name='book-form'),
    path('library/stats/', views.library_stats, name='librarystats'),
    path('book/', views.BookListView.as_view(), name='book-list'),
    path('book/list/', views.BookListView.as_view(), name='book-list'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('cart/', views.CartListView.as_view(), name='cart-list')
    # path('book/list/genre/', views.BookByGenreListView.as_view(), name='book-list-genre'),

]
