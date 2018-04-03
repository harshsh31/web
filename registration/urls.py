from django.urls import path
from . import views
app_name = 'registration'
urlpatterns = [
    path('register/', views.user_registration, name="register"),
    path('check-username', views.check_username, name="check-username"),
    path('check-email', views.check_email, name="check-email"),
]
