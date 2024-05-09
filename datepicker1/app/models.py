# datetimepicker_app/models.py
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class SelectedDate(models.Model):
    selected_date = models.DateField()

    def __str__(self):
        return str(self.selected_date)

class SelectedTime(models.Model):
    selected_time = models.TimeField()

    def __str__(self):
        return str(self.selected_time)
    


