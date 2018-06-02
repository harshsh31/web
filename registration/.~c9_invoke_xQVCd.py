from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'registration'
urlpatterns = [
    path('register/', views.user_registration, name="register"),
    path('check-username', views.check_username, name="check-username"),
    path('check-email', views.check_email, name="check-email"),
    path('submit_post', views.submit_post, name='submit_post'),
    path('city_count', views.city_country, name='city-count'),
    path('otp-verify',views.otp_verify, name='otp-verify'),
]
