import django.contrib.auth.views
from django.urls import path
from . import views

app_name = 'twitterManager'
urlpatterns = [
    path('', django.contrib.auth.views.LoginView.as_view(
        template_name='login.html')),
]
