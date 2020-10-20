from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from crossword_puzzle.models import Thirdyear

def puzzle_view(request):
	return render(request, 'crossword_begining.html', {'row': 15})

def age_sum(request):
	return render(request, 'agesum.html')

def bridge_connect(request):
	return render(request, 'bridgeconnect.html')

def slither_link(request):
	return render(request, 'slitherlink.html')

def submission(request):
	if request.method == "POST":
		crossword = request.POST.get('submittedCrossword')
		print(crossword)
		agesum_solved = request.POST.get('is_agesum_solved')
		letter_sum_solved = request.POST.get('is_lettersum_solved')
		puzzle_score = request.POST.get('puzzle_score')
		# thirdyear = Thirdyear.objects.filter(user=request.user)
		# thirdyear.puzzle_score = puzzle_score
		# thirdyear.age_sum = agesum_solved
		# thirdyear.save()

		thirdyear = Thirdyear(puzzle_score=puzzle_score, age_sum=agesum_solved, letter_sum=letter_sum_solved)
		thirdyear.save()
		data = "Save Successfully"
		return JsonResponse(data, safe=False)

	return HttpResponse("get method")

def login(request):
	pass
