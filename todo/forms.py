from django import forms
from .models import Task


class TaskForm(forms.ModelForm):    
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'Task title',
                'hx-post': '/check_task_title/',
                'hx-trigger': 'keyup changed delai:1s',
                'hx-target': '#title-errors',
                'hx-swap': 'outerhtml',
            }),
            'description': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'Description',
                'rows': '3'
            }),
            'status': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
            }),
            'date': forms.SelectMultiple(attrs={
                'class': "custom-select-multiple",
            }),
        }
