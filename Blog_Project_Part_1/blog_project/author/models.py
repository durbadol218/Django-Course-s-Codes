from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    phone_no = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    