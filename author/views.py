from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show_authors(request):
    return HttpResponse('<h1>Author Page</h1>')