# calendarapp/models.py
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
