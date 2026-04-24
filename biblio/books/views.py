from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book


# Create your views here.


def books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "show.html", context)


def getName(request):
    if request.method == "GET":
        b = Book.objects.get(id = 1)
        bb = Book.objects.get(name__starts_with = "A")
        bbb = Book.objects.get(code__contains = 2)
        
        books = Book.objects.all()
        
        nb = Book.objects.create(
            name = "da",
            description = "sdfgdsgfdg",
            code = 12
        )
        
        newb = Book("aad","adfghdfgh",12)
        
        newb.save()
        
        nb.delete()
        
        fb = Book.objects.filter()