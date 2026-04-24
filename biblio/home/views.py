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




