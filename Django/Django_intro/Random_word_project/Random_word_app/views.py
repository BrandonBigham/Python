from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'num' in request.session:
        request.session['num'] += 1
    else:
        request.session['num'] = 0
    return render(request, 'index.html')

def random_word(request):
    if request.method == "POST":
        request.session['string'] = get_random_string(length=10)
    else:
        return redirect("/")
    return redirect("/")

def reset(request):
    if request.method == "POST":
        del request.session['num']
        del request.session['string']
    else:
        return redirect("/")
    return redirect('/')

# Create your views here.
