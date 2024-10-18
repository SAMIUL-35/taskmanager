# forms.py
from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'  
        widgets = {
            'task_title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter task title'
            }),
            'task_description': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter task description', 
                'rows': 3
            }),
            'assign_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
            }),
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'categories': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-control',  
                
            }),
        }
