# datetimepicker_app/models.py
from django.db import models


class SelectedDate(models.Model):
    selected_date = models.DateField()

    def __str__(self):
        return str(self.selected_date)

