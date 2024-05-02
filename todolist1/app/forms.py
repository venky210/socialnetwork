from django import forms

from app.models import *

class userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':''}

class todolistform(forms.ModelForm):
    class Meta:
        model=Todolist
        fields='__all__'