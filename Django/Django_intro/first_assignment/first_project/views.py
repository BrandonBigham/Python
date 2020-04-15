from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display a list of blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(response):
    return redirect("/")

def show(response, number):
    return HttpResponse("placeholder to display blog number: " + number)

def edit(response, number):
    return HttpResponse("placeholder to edit blog " + number)

def destroy(response, number):
    return redirect("/")

def delete(response, number):
    return redirect("/")

# Create your views here.
