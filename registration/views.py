from django.shortcuts import render
from . import models
import json
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404, _get_queryset, HttpResponse
from django.http import JsonResponse
from datetime import datetime,date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import random
from pprint import pprint
import zerosms

# Create your views here.

def user_registration(request):
    if request.method == 'GET':
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
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
@csrf_exempt
def submit_post(request):
    if request.method == 'POST':
        data = json.loads(request.POST['data'])
        user = User()
        user.username = data['user']
        user.email = data['email']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.set_password(data['pass'])

        userprofile = models.UserProfile()

        userprofile.middle_name = data['middle_name']
        userprofile.address = data['address']
        userprofile.pin_no = int(data['pincode'])
        userprofile.city = data['city']
        userprofile.contact_no = int(data['phone'])
        userprofile.country = data['country']
        ip = request.META['REMOTE_ADDR']
        userprofile.ip_address = ip
        pprint(userprofile.__dict__)
        user.save()
        userprofile.save()
        userprofile.user = user
        userprofile.save()
        userprofile.send_activation_email()
        userprofile.send_otp()
        return HttpResponse("success")


def city_country(request):
    if request.method == 'GET':
        city = models.Cities.objects.all()
        cities = []
        countries =[]
        for c in city:
            cities.append(c.city)
        country = models.Country.objects.all()
        for c in country:
            countries.append(c.country)
        data = {
            'city': cities,
            'country': countries,
        }
        return HttpResponse(json.dumps(data))

