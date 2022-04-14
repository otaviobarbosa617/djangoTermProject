from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookForm

def index(request):
    context = {}
    context['form'] = BookForm()
    return render(request, 'home.html', context)

