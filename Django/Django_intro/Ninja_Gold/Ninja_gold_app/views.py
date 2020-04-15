from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
    if 'gold' not in request.session:
        request.session["gold"] = 0
        request.session['activity']=[]
    return render(request, "index.html")

def process(request):
    if request.method == "POST":
        if request.POST["building"] == "Farm":
            temp = random.randint(10,20)
            request.session['gold'] += temp
            request.session['activity'].append("you gained " + str(temp) + " gold")
        if request.POST["building"] == "Cave":
            temp = random.randint(5,10)
            request.session['gold'] += temp
            request.session['activity'].append("you gained " + str(temp) + " gold")
        if request.POST["building"] == "House":
            temp = random.randint(-5,-2)
            request.session['gold'] += temp
            request.session['activity'].append("you lost " + str(-temp) + " gold")
        if request.POST["building"] == "Casino":
            temp = random.randint(-1000,1000)
            request.session['gold'] += temp
            if temp > 0:
                request.session['activity'].append("you gained " + str(temp) + " gold")
            if temp < 0:
                request.session['activity'].append("you lost " + str(-temp) + " gold")
        if request.POST["building"] == "reset":
            del request.session['gold']
            del request.session['activity']
    return redirect('/')

def wrong(request, route):
    print('undefined URL')
    return redirect('/')
# Create your views here.
