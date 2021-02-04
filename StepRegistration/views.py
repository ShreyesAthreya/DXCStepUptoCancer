from django.contrib import messages, auth
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth import get_user_model
# Create your views here.
from .forms import CreateStepsForm, UpdateStepForm
from .models import Step


def addSteps(request):
    form = CreateStepsForm()

    if request.method == 'POST':
        try:
            request.POST = request.POST.copy()
            form = CreateStepsForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                messages.success(request, "You have added your steps successfully!")
            return redirect("home")
        except IntegrityError:
            messages.error(request, "You already have steps created. Go to the homepage to edit em !")
            return redirect("add-steps")

    context = {'form': form}
    return render(request, 'StepRegistration/addSteps.html', context)


class HomeView(ListView):
    model = Step
    template_name = 'StepRegistration/index.html'
    ordering = ['-steps']

    def get_context_data(self, **kwargs):
        User = get_user_model()
        context = super().get_context_data(**kwargs)
        context["qs"] = Step.objects.all()
        context['TeamDXC'] = Step.objects.all().values()
        TeamDXC = User.objects.filter(is_DXC=True)
        TeamAmey = User.objects.filter(is_DXC=False)
        DXCSteps = 0
        AmeySteps = 0

        try:
            for user in TeamAmey:
                userID = User.objects.get(username=user).id
                Steps = Step.objects.filter(user_id=userID).values('steps').values_list('steps', flat=True)
                AmeySteps += Steps[0]

            for user in TeamDXC:
                userID = User.objects.get(username=user).id
                Steps = Step.objects.filter(user_id=userID).values('steps').values_list('steps', flat=True)
                print(DXCSteps)
                DXCSteps += Steps[0]
            context['DXC'] = DXCSteps
            context['Amey'] = AmeySteps
        except:
            pass
        return context


class StepDetailView(DetailView):
    model = Step
    template_name = 'StepRegistration/viewSteps.html'


class UpdateStepView(UpdateView):
    model = Step
    template_name = 'StepRegistration/updateSteps.html'
    form_class = UpdateStepForm
