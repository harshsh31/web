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
    path('password/change/',
        auth_views.PasswordChangeView.as_view(),
        name='password_change'),
    path('password/change/done/',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),
    path('password/reset/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    path('password/reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    re_path('password/reset/\
        (?P<uidb64>[0-9A-Za-z_\-]+)/\
        (?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),

    re_path(r'^password/reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),

]
