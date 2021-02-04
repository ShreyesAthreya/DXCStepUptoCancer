from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('Register/', views.register, name='register'),
    path('Signin/', views.sign_in, name='sign-in'),
    path('logout/', views.logout, name='logout'),
]
