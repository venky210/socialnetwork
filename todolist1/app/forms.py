from django import forms

from app.models import *

class userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':''}

class TaskForm(forms.ModelForm):
    is_task = forms.BooleanField(label='Task is completed',required=False)
    class Meta:
        model=Task
        fields=['title', 'description','is_task']                                                     