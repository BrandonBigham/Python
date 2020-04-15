from django.shortcuts import render, redirect
from .models import User, Post
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
            user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], password=hashed_pw, email=request.POST['email'])
            print("User's password has been changed to " + user.password)
    return redirect('/')

def login(request):
    if request.method == "POST":
        users_with_email = User.objects.filter(email=request.POST['email'])
        if users_with_email:
            user = users_with_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/homepage')
            else:
                print("Password didn't match")
                messages.error(request, "Incorrect name or password")
        else:
            print("Name not found")
            messages.error(request, "Incorrect email or password")
    return redirect('/')

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/')

def homepage(request):
    if 'user_id' not in request.session:
        messages.error(request, 'you must be logged in')
        return redirect('/')
    else:
        context = {
            'all_posts': Post.objects.annotate(number_of_likes=Count('likes')),
            "user": User.objects.get(id=request.session['user_id'])
        }
        return render(request, "homepage.html", context)

def createCat(request):
    if request.method == "POST":
        errors = Post.objects.post_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            Post.objects.create(quote=request.POST['quote'], author=User.objects.get(id=request.session['user_id']))
    return redirect('/homepage')