from django import forms
from .models import Category

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['Category']  

    
    




