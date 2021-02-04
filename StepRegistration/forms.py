from django import forms

from .models import Step


class CreateStepsForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ('Day_1', 'Day_2', 'Day_3', 'Day_4', 'Day_5', 'Day_6', 'Day_7')

        widgets = {
            'Day_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Day_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Day_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Day_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Day_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Day_6': forms.TextInput(attrs={'class': 'form-control'}),
            'Day_7': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'Day_1': 'Day 1',
            'Day_2': 'Day 2',
            'Day_3': 'Day 3',
            'Day_4': 'Day 4',
            'Day_5': 'Day 5',
            'Day_6': 'Day 6',
            'Day_7': 'Day 7',
        }


class UpdateStepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ('Day_1', 'Day_2', 'Day_3', 'Day_4', 'Day_5', 'Day_6', 'Day_7')

        widgets = {
            'Day_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Day_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Day_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Day_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Day_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Day_6': forms.TextInput(attrs={'class': 'form-control'}),
            'Day_7': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'Day_1': 'Day 1',
            'Day_2': 'Day 2',
            'Day_3': 'Day 3',
            'Day_4': 'Day 4',
            'Day_5': 'Day 5',
            'Day_6': 'Day 6',
            'Day_7': 'Day 7',
        }
