from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from payback.models import *
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
    technoplayer1 = Technoplayer1.objects.filter(user=request.user).first()
    loan2 = technoplayer1.loan1
    connection2 = technoplayer1.connection1
    happiness2 = technoplayer1.happiness1
    focus2 = technoplayer1.focus1
    return render(request, 'secondyear.html', {'loan2': loan2, 'connection2': connection2, 'happiness2': happiness2,'focus2':focus2})


def thirdyear(request):
    technoplayer2 = Technoplayer2.objects.filter(user=request.user).first()
    loan3 = technoplayer2.loan2
    connection3 = technoplayer2.connection2
    happiness3 = technoplayer2.happiness2
    focus3 = technoplayer2.focus2
    return render(request, 'thirdyear.html',{'loan3': loan3, 'connection3': connection3, 'happiness3': happiness3,'focus3':focus3})


def fourthyear(request):
    technoplayer3 = Technoplayer3.objects.filter(user=request.user).first()
    loan4 = technoplayer3.loan3
    connection4 = technoplayer3.connection3
    happiness4 = technoplayer3.happiness3
    focus4 = technoplayer3.focus3
    return render(request, 'fourthyear.html',{'loan4': loan4, 'connection4': connection4, 'happiness4': happiness4,'focus4':focus4})


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
    technoplayer1 = Technoplayer1.objects.filter(user=request.user).first()
    if request.method == "POST":
        focus = request.POST.get('focus')
        happiness = request.POST.get('happiness')
        connection = request.POST.get('connection')
        loan = request.POST.get('loan')
        print(focus)
        print(loan)
        if technoplayer1 is None:
            print(1)
            technoplayer1.user = request.user
            technoplayer1.happiness1 = happiness
            technoplayer1.connection1 = connection
            technoplayer1.focus1 = focus
            technoplayer1.loan1 = loan
            technoplayer1.save()
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
        return redirect(request.GET.get('next', '/firstyear'))

    if request.method == "POST":
        technouser = User.objects.filter(roll_no=request.POST['roll_no']).first()
        if technouser is None:
            return render(request, 'login.html', {"messages": [["text-danger", "Roll Number Not Found."]]})
        username = technouser.username
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Used logged in!")
            return redirect(request.GET.get('next', '/firstyear'))
        else:
            return render(request, 'login.html', {"messages": [["text-danger", "Invalid Credentials."]]})
    return render(request, 'login.html', )


def logout_view(request):
    logout(request)
    return redirect('/')


def secondyear_submission(request):
    if request.method == "POST":
        focus = request.POST.get('focus')
        print(focus)
        happiness = request.POST.get('happiness')
        connection = request.POST.get('connection')
        loan = request.POST.get('loan')
        technoplayer2 = Technoplayer2.objects.filter(user=request.user)
        if technoplayer2 is not None:
            pass
            # technoplayer1.happiness = happiness
            # technoplayer1.connection = connection
            # technoplayer1.focus = focus
            # technoplayer1.loan = loan
            # technoplayer1.save()
        else:
            technoplayer2.user = request.user
            technoplayer2.happiness2 = happiness
            technoplayer2.connection2 = connection
            technoplayer2.focus2 = focus
            technoplayer2.loan2 = loan
            technoplayer2.save()

        # thirdyear = Thirdyear(puzzle_score=puzzle_score, age_sum=agesum_solved, letter_sum=letter_sum_solved)
        # thirdyear.save();
        data = "Save Successfully"
        return JsonResponse(data, safe=False)

    return HttpResponse("get method")


def thirdyear_submission(request):
    if request.method == "POST":
        focus = request.POST.get('focus')
        print(focus)
        happiness = request.POST.get('happiness')
        connection = request.POST.get('connection')
        loan = request.POST.get('loan')
        technoplayer3 = Technoplayer3.objects.filter(user=request.user)
        if technoplayer3 is not None:
            pass
            # technoplayer1.happiness = happiness
            # technoplayer1.connection = connection
            # technoplayer1.focus = focus
            # technoplayer1.loan = loan
            # technoplayer1.save()
        else:
            technoplayer3.user = request.user
            technoplayer3.happiness3 = happiness
            technoplayer3.connection3 = connection
            technoplayer3.focus3 = focus
            technoplayer3.loan3 = loan
            technoplayer3.save()

        # thirdyear = Thirdyear(puzzle_score=puzzle_score, age_sum=agesum_solved, letter_sum=letter_sum_solved)
        # thirdyear.save();
        data = "Save Successfully"
        return JsonResponse(data, safe=False)

    return HttpResponse("get method")


def fourthyear_submission(request):
    if request.method == "POST":
        focus = request.POST.get('focus')
        print(focus)
        happiness = request.POST.get('happiness')
        connection = request.POST.get('connection')
        loan = request.POST.get('loan')
        technoplayer4 = Technoplayer4.objects.filter(user=request.user)
        if technoplayer4 is not None:
            pass
            # technoplayer1.happiness = happiness
            # technoplayer1.connection = connection
            # technoplayer1.focus = focus
            # technoplayer1.loan = loan
            # technoplayer1.save()
        else:
            technoplayer4.user = request.user
            technoplayer4.happiness4 = happiness
            technoplayer4.connection4 = connection
            technoplayer4.focus4 = focus
            technoplayer4.loan4 = loan
            technoplayer4.save()

        # thirdyear = Thirdyear(puzzle_score=puzzle_score, age_sum=agesum_solved, letter_sum=letter_sum_solved)
        # thirdyear.save();
        data = "Save Successfully"
        return JsonResponse(data, safe=False)

    return HttpResponse("get method")
