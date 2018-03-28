from django.shortcuts import render
from . import models
import json
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404, _get_queryset, HttpResponse
from . import forms
from django.http import JsonResponse
from pprint import pprint
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def user_registration(request):
    if request.method == 'GET':
        return render(request,'registration/signup.html',{})

def check_username(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if models.UserProfile.objects.filter(user__username=username).exists():
            return HttpResponse("username not available")
        else:
            return HttpResponse("username available")
