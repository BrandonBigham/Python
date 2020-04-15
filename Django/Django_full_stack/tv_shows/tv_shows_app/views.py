from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

def index(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, 'shows.html', context)
def addshow(request):
    return render(request, 'add_show.html')
def createshow(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/add/show')
    if request.method == "POST":
        Show.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            network = request.POST['network'],
            release_date = request.POST['release_date']
        )
    return redirect(f'/show/info/{id}')
def editshow(request, id):
    context = {
        "show": Show.objects.get(id=id),
    }
    return render(request, 'edit_show.html', context)
def showinfo(request, id):
    context = {
        "show": Show.objects.get(id=id),
    }
    return render(request, 'show_info.html', context)
def editshowproccess(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/show/{id}')
    if request.method == "POST":
        show_to_update = Show.objects.get(id=id)
        show_to_update.title = request.POST['title']
        show_to_update.network = request.POST['network']
        show_to_update.release_date = request.POST['release_date']
        show_to_update.description = request.POST['description']
        show_to_update.save()
    return redirect(f'/show/info/{id}')
def deleteshow(request, id):
    show_to_delete = Show.objects.get(id=id)
    show_to_delete.delete()
    return redirect('/shows')

def direct(request):
    return redirect('/shows')

# Create your views here.
