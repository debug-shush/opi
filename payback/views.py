from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from payback.models import Technoplayer
from .models import *


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
    technoplayer = Technoplayer.objects.filter(user=request.user).first()
    loan = technoplayer.loan
    connection = technoplayer.connection
    happiness= technoplayer.happiness
    return render(request, 'secondyear.html',{'loan':loan,'connection':connection,'happiness':happiness})


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
    technoplayer = Technoplayer.objects.filter(user=request.user).first()
    if request.method == "POST":
        focus = request.POST.get('focus')
        happiness = request.POST.get('happiness')
        connection = request.POST.get('connection')
        loan = request.POST.get('loan')
        print(focus)
        if technoplayer is not None:
            technoplayer.happiness = happiness
            technoplayer.connection = connection
            technoplayer.focus = focus
            technoplayer.loan = loan
            technoplayer.save()
        else:
            technoplayer = Technoplayer()
            technoplayer.user = request.user
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


# def login(request):
#     if request.method == 'POST':
#         rollno = (request.POST['rollno'])
#         password = (request.POST['password'])
#         technoplayer = Technoplayer.objects.get(rollno=rollno)
#         # user = authenticate(rollno = rollno, password=password)
#         if technoplayer is not None:
#             print('user logged in')
#             return JsonResponse("Login Successful",safe=False)

def techo_login(request):
    if request.user.is_authenticated:
        return redirect(request.GET.get('next','/firstyear'))

    if request.method=="POST":
        technouser = User.objects.filter(roll_no=request.POST['roll_no']).first()
        if technouser is None:
            return render(request, 'login.html', {"messages":[["text-danger","Roll Number Not Found."]]})
        username = technouser.username;
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Used logged in!")
            return redirect(request.GET.get('next','/firstyear'))
        else:
            return render(request, 'login.html',{"messages":[["text-danger","Invalid Credentials."]]})
    return render(request, 'login.html',)


def logout_view(request):
    logout(request)
    return redirect('/')
