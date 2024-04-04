# forms.py
from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email','role']
        
class DealerRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email','role']

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['name', 'price', 'quantity','image']        