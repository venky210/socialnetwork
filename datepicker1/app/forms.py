# datetimepicker_app/forms.py
from django import forms
from .models import SelectedDate

class DateForm(forms.ModelForm):
    class Meta:
        model = SelectedDate
        fields = ['selected_date']
        widgets = {
            'selected_date': forms.DateInput(attrs={'type': 'date'})
        }
