from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.forms.models import model_to_dict
from django.core import serializers
import json
from django.conf import settings
from django.template.loader import render_to_string

def home(request):
	return render(request, 'index.html')