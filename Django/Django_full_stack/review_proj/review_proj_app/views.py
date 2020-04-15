from django.shortcuts import render, redirect
from .models import User, Cat
from django.contrib import messages
import bcrypt
from django.db.models import Count

def index(request):
    return render(request, "index.html")

def createUser(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            print("User's password entered was " + request.POST['password'])
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(name=request.POST['name'], password=hashed_pw)
            print("User's password has been changed to " + user.password)
    return redirect('/')

def login(request):
    if request.method == "POST":
        users_with_name = User.objects.filter(name=request.POST['name'])
        if users_with_name:
            user = users_with_name[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                request.session['user'] = user.name #IMPORTANT!!!
                return redirect('/homepage')
            else:
                print("Password didn't match")
                messages.error(request, "Incorrect name or password")
        else:
            print("Name not found")
            messages.error(request, "Incorrect name or password")
    return redirect('/')

def homepage(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        context = {
            'all_cats': Cat.objects.annotate(votes=Count('users_that_voted')).order_by('-votes'),
            "user": User.objects.get(id=request.session['user_id'])
        }
        return render(request, "main_page.html", context)

def createCat(request):
    if request.method == "POST":
        errors = Cat.objects.cat_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            Cat.objects.create(name=request.POST['name'], owner=User.objects.get(id=request.session['user_id']))
    return redirect('/homepage')

def deletecat(request, id):
    if request.method == "POST":
        cat_with_id = Cat.objects.filter(id=id)
        if cat_with_id:
            cat = cat_with_id[0]
            user = User.objects.get(id=request.session['user_id'])
            if cat.owner == user:
                cat.delete()
    return redirect('/homepage')

def votecat(request, id):
    if request.method == "POST":
        cat_with_id = Cat.objects.filter(id=id)
        if cat_with_id:
            cat = cat_with_id[0]
            user = User.objects.get9id=request.session['user_id']
            cat.users_that_voted.add(user)
    return redirect('/homepage')

def unvotecat(request, id):
    if request.method == "POST":
        cat_with_id = Cat.objects.filter(id=id)
        if cat_with_id:
            cat = cat_with_id[0]
            user = User.objects.get9id=request.session['user_id']
            cat.users_that_voted.remove(user)
    return redirect('/homepage')

def userprofile(request):
    if 'user_id' in request.session:
        context = {
            "user": User.objects.get(id=request.session['user_id'])
        }
        return render(request, "one_user.html", context)
    return redirect('/')

def catprofile(request, id):
    if 'user_id' in request.session:
        cat_with_id = Cat.objects.filter(id=id)
        if cat_with_id:
            context = {
                "cat": Cat.objects.get(id=id)
            }
            return render(request, "one_cat.html", context)
    return redirect('/')
