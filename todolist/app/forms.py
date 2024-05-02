from app.models import *
from django import forms


class RegistrationForm(forms.ModelForm):
    
    class Meta:
        model = UserRegister
        fields = ["username",'password']
        widgets={'password':forms.PasswordInput}

