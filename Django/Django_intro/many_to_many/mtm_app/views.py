from django.shortcuts import render, redirect
from .models import Owner
from django.contrib import messages

def index (request):
    return render(request, "index.html")

def createowner(request):
    errors = Owner.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    Owner.objects.create(name=request.POST["name"], age=request.POST["age"])
    return redirect('/success')

def success(request):
    return render(request, "success.html")

# Create your views here.
