from django.shortcuts import render
from django.http import HttpResponse
from .models import Order, CustomUser, Book
from datetime import datetime

# Create your views here.
def show_orders(request):
    if request.method == 'POST':
        currentDate = datetime.today().strftime('%Y-%m-%d')
        name = request.POST.get("name")
        email = request.POST.get("email")
        book = request.POST.get("book")
        Order.create(CustomUser.objects.get(first_name=name, email=email), Book.objects.filter(name=book)[0], currentDate)
    return render(request, "order_form.html" ,{})