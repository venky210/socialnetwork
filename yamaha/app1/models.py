from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        USER = 'USERS', 'Users'
        DEALER = 'DEALER', 'Dealer'

    role = models.CharField(max_length=70, choices=Role.choices, default=Role.USER)
    dealer_field = models.CharField(max_length=100, blank=True, null=True)

    def _str_(self):
        return self.username