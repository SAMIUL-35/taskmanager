from django import forms
from .models import CategoryModel

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = '__all__'  
        
        widgets = {
            'category_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter Category Name'
            }),
            
           
        }
