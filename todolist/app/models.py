from django.db import models
# from django.contrib.auth.models import User


class UserRegister(models.Model):
    username=models.CharField(max_length=100)
    password=models.IntegerField(max_length=100)

class TodoItem(models.Model):
    user = models.ForeignKey(UserRegister, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
