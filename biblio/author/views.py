from django.shortcuts import render, get_object_or_404
from .models import Author

# Create your views here.
# =========================
# AUTHOR VIEWS
# =========================

def author_list(request):

    authors = Author.objects.all()

    context = {
        "authors": authors
    }

    return render(
        request,
        "authors/author_list.html",
        context
    )


def author_detail(request, id):

    author = get_object_or_404(
        Author,
        id=id
    )

    context = {
        "author": author
    }

    return render(
        request,
        "authors/author_detail.html",
        context
    )
