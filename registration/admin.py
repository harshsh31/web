from django.contrib import admin
from .models import UserProfile,Cities,State,Country
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Cities)
admin.site.register(State)
admin.site.register(Country)