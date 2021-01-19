#from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render
from django.utils.crypto import get_random_string


def some_function(request):
    request.session['name'] = request.POST['name']
    request.session['counter'] = 100

def index(request):
    request.session['counter'] = 0
    return render(request, 'index.html')

def random(request):
    request.session['counter'] += 1
    context = {
        "palabra": get_random_string(length=14)
    }
    return render(request, 'index.html', context)


