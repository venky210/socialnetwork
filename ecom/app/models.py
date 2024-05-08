from django.db import models

class Category(models.Model):
    Category = models.CharField(max_length=100)
    
    # Add more fields as needed

    def __str__(self):
        return self.Category



