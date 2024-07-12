from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category) # ekta post multiple category'r moddhe thaakte paare, abaar akta category'r moddhe multiple post thaakte paare!
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    