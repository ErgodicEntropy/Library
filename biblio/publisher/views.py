from django.shortcuts import render, get_object_or_404
from .models import Publisher

# Create your views here.


# =========================
# PUBLISHER VIEWS
# =========================

def publisher_list(request):

    publishers = Publisher.objects.all()

    context = {
        "publishers": publishers
    }

    return render(
        request,
        "publishers/publisher_list.html",
        context
    )


def publisher_detail(request, id):

    publisher = get_object_or_404(
        Publisher,
        id=id
    )

    context = {
        "publisher": publisher
    }

    return render(
        request,
        "publishers/publisher_detail.html",
        context
    )

