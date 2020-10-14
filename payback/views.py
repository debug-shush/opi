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

def secondyear(request):
    return render(request, 'thirdyear.html')

def secondyear(request):
    return render(request, 'fourthyear.html')