from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Home


# Create your views here.

def home(request):
    return HttpResponse('<p>Hello World!</p>') 


def getHomes(request):
    if request.method == "GET":
        homes = Home.objects.all() #ORM query
        return render(request, "home.html", {"homes": homes})


def getTitle(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        
        Home.objects.create(
            title = title,
            description = description
        )
        return redirect('home')
        
    return render(request,"home.html", {})


from django.shortcuts import render, get_object_or_404
from .models import Home


# =========================
# HOME VIEWS
# =========================

def home_list(request):

    homes = Home.objects.all()

    context = {
        "homes": homes
    }

    return render(
        request,
        "home/home_list.html",
        context
    )


def home_detail(request, id):

    home = get_object_or_404(
        Home,
        id=id
    )

    context = {
        "home": home
    }

    return render(
        request,
        "home/home_detail.html",
        context
    )

