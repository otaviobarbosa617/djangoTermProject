from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('addbook',views.add_book, name='addbook'),
    path('allbooks', views.view_all_books, name='allbooks'),
    path('librarystats', views.library_stats, name='librarystats')
]
