from django.shortcuts import render
from . import models
import json
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404, _get_queryset, HttpResponse
from django.http import JsonResponse
from pprint import pprint
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def user_registration(request):
    if request.method == 'GET':
        return render(request,'registration/signup.html',{})
@csrf_exempt
def check_username(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(request.POST.get('username'))
        if models.UserProfile.objects.filter(user__username=username).exists():
            return HttpResponse("0")
        else:
            return HttpResponse("1")

@csrf_exempt
def check_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(request.POST.get('email'))
        if models.UserProfile.objects.filter(user__email=email).exists():
            return HttpResponse("0")
        else:
            return HttpResponse("1")
