# forms.py
from django import forms
from .models import User
from django.contrib.auth import login, authenticate

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

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.is_active:
                raise forms.ValidationError("Invalid username or password.")

        return cleaned_data