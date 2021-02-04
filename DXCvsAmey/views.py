from django.contrib import messages, auth
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView


def home(request):
    return render(request, 'base.html')
