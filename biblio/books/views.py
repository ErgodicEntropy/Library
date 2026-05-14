from django.shortcuts import render, get_object_or_404, redirect
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
        
        

# =========================
# BOOK VIEWS
# =========================

def book_list(request):

    books = Book.objects.all()

    context = {
        "books": books
    }

    return render(
        request,
        "books/book_list.html",
        context
    )


def book_detail(request, id):

    book = get_object_or_404(
        Book,
        id=id
    )

    context = {
        "book": book
    }

    return render(
        request,
        "books/book_detail.html",
        context
    )

