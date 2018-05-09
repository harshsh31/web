from django.db import models
from django.contrib.auth.models import User
from .utils import code_generator
from django.core.mail import send_mail
from django.conf import settings
import random
import zerosms
# Create your models here.


class UserProfile(models.Model):
	DESIGNATION = (
		('Lawyer','Lawyer'),
		('Doctor','Doctor'),
		('Officer','Ofiicer'),
	)
	GENDER = (
		('male','male'),
		('female', 'female'),
		('other', 'other'),
	)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	middle_name = models.CharField(max_length=255, null=True, blank=True)
	gender = models.CharField(max_length=255, choices=GENDER)
	designations = models.CharField(max_length=255, null=True, blank=True,choices=DESIGNATION)
	contact_no = models.BigIntegerField(unique=True)
	address = models.CharField(max_length=500,null=True,blank=True)
	pin_no = models.IntegerField(null=True, blank=True)
	city = models.CharField(max_length=255, null=True,blank=True)
	country = models.CharField(max_length=255, null=True, blank=True)
	reference = models.CharField(max_length=255, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	ip_address = models.GenericIPAddressField(null=True,blank=True)
	activation_key=models.CharField(max_length=250,null=True,blank=True)
	otp=models.CharField(max_length=250,null=True,blank=True)
	activated=models.BooleanField(default=False)

	def __str__(self):
		return self.user.username
	def send_activation_email(self):
	        if not self.activated:
	            self.activation_key=code_generator()
	            self.save()
	            subject = 'Ani email activation'
	            from_email = settings.DEFAULT_FROM_EMAIL
	            message = f'activate your account here: {self.activation_key}'
	            recipient_list = [self.user.email]
	            html_message = f'<p>activate your account here: {self.activation_key}</p>'
	            sent_mail=send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
	            return sent_mail
	def send_otp(self):
		sender = "8097707287"
		password = "harshshah31"
		otp = random.randrange(100000,999999,1)
		self.otp = otp
		self.save()
		msg = "Your otp is" + str(otp)
		zerosms.sms(phno=sender,passwd=password,receivernum=self.contact_no,message=msg)


class Cities(models.Model):
	city = models.CharField(max_length=255,null=True,blank=True)
	def __str__(self):
		return self.city

class State(models.Model):
	state = models.CharField(max_length=255,null=True,blank=True)
	def __str__(self):
		return self.state

class Country(models.Model):
	country = models.CharField(max_length=255,null=True,blank=True)
	def __str__(self):
		return self.country

