from django.db import models
from datetime import datetime
# Create your models here.
class CarBrand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True,null=True,blank=True)
    
    def __str__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(max_length=255)
    brand_name = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    color = models.CharField(max_length=255)
    description = models.TextField(blank= True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=3)
    image = models.ImageField(upload_to='cars/upload/car_images/', blank= True, null=True)
    quantity = models.IntegerField(default=0)
    
    
    def __str__(self):
        return f"{self.name}"

class CommentModel(models.Model):
    car_post = models.ForeignKey(CarModel,related_name= "comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    comment_body = models.TextField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"Comments by {self.name}"