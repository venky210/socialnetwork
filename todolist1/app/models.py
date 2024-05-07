from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=100)
    datetime=models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)  
   


    def __str__(self):
        return self.title
