from django.urls import path

from . import views
from .views import HomeView, StepDetailView, UpdateStepView

urlpatterns = [
    path('addsteps/', views.addSteps, name='add-steps'),
    path('', HomeView.as_view(), name='home'),
    path('viewsteps/<int:pk>', StepDetailView.as_view(), name='view-steps'),
    path('updatesteps/<int:pk>', UpdateStepView.as_view(), name='update-steps'),
]
