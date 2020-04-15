from django.shortcuts import render, HttpResponse, redirect
from .models import Shoe

def index(request):
    context = {
        "all_shoes": Shoe.objects.all()
    }
    return render(request, "index.html", context)

def process(request):
    return redirect("/")
# Create your views here.
