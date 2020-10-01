from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def opening(request):
    return render(request, 'opening.html')

def firstyear(request):


    return render(request, 'firstyear.html')
