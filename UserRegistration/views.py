from django.contrib import messages, auth
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.shortcuts import render, redirect
from StepRegistration.models import Step


def register(request):
    if request.method == 'POST':
        User = get_user_model()
        first_name = str(request.POST['first_name']).capitalize()
        last_name = str(request.POST['last_name']).capitalize()
        username = str(request.POST['username']).lower()
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        is_DXC = request.POST['isDXC']
        my_list = [first_name, last_name, password1, password2]
        if is_DXC == 'True':
            is_DXC = True
        else:
            is_DXC = False
        print(is_DXC)

        if '' in my_list:
            return render(request, 'UserRegistration/register.html', {'error': 'Fields can\'t be blank'})

        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                password=password1, is_DXC=is_DXC)
                user.save()
                messages.success(request, "You have registered successfully!")
                login(request, user)
                return redirect("add-steps")
            except ValueError:
                return render(request, 'UserRegistration/register.html', {'error': 'Username can\'t be blank'})

            except IntegrityError:
                return render(request, 'UserRegistration/register.html',
                              {'error': 'Username already exists. Please choose another'})
        else:
            return render(request, 'UserRegistration/register.html', {'error': 'Passwords did not match'})

    else:
        return render(request, 'UserRegistration/register.html')


def sign_in(request):
    if request.method == 'POST':
        username = str(request.POST['username']).lower()
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user:
            login(request, user)
            ifUserSteps = Step.objects.filter(user=user.id).values()
            if ifUserSteps:
                print("yes")
                return redirect("home")
            else:
                print("no")
                return redirect("add-steps")
        else:
            messages.error(request, "Unable to verify username and password")
            return redirect('sign-in')

    return render(request, 'UserRegistration/sign_in.html')


def logout(request):
    auth.logout(request)
    messages.success(request, "You have logged out successfully!")
    return redirect("/")
