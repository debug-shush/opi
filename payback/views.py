from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def opening(request):
    return render(request, 'opening.html')

def firstyear(request):
    return render(request, 'firstyear.html')

def kenken(request):
    return render(request, 'kenken.html')

def slidepuzzle(request):
    return render(request, 'slidingpuzzle.html')


def slider(request):
    return render(request, 'slider.html')

def tangram(request):
    return render(request, 'tangram.html')

def secondyear(request):
    return render(request, 'secondyear.html')

def thirdyear(request):
    return render(request, 'thirdyear.html')

def fourthyear(request):
    return render(request, 'fourthyear.html')

def graduation(request):
    return render(request, 'graduation.html')

def game(request):
    return render(request, 'game.html')