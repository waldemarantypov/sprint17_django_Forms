from django.shortcuts import render
from django.http import HttpResponse
from book.models import Book


# Create your views here.
def show_books(request):
    randomBooks = Book.objects.all().order_by('?')[:3]
    context = {"allBooks": randomBooks}
    return render(request, 'index.html', context)
