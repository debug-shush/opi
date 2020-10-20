from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from payback.models import Technoplayer


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


def mastermind(request):
    return render(request, 'mastermind.html')


def crossword(request):
    return render(request, 'crossword_begining.html')


def mysteryroom(request):
    return render(request, 'mystery_room.html')


def firstyear_submission(request):
    if request.method == "POST":
        focus = request.POST.get('focus')
        print(focus)
        happiness = request.POST.get('happiness')
        connection = request.POST.get('connection')
        loan = request.POST.get('loan')
        technoplayer = Technoplayer.objects.filter(user=request.user)
        if technoplayer != None:
            technoplayer.happiness = happiness
            technoplayer.connection = connection
            technoplayer.focus = focus
            technoplayer.loan = loan
            technoplayer.save()

        # thirdyear = Thirdyear(puzzle_score=puzzle_score, age_sum=agesum_solved, letter_sum=letter_sum_solved)
        # thirdyear.save();
        data = "Save Successfully"
        return JsonResponse(data, safe=False)

    return HttpResponse("get method")


def login(request):
    if request.method == 'POST':
        rollno = (request.POST['rollno'])
        password = (request.POST['password'])
        user = authenticate(rollno = rollno, password=password)
        if user is not None:
            print('user logged in')
            return redirect('firstyear.html')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/')
    else:
        return render(request, 'opening.html')
