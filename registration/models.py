from django.db import models
from django.contrib.auth.models import User

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

	def __str__(self):
		return self.user.username


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

