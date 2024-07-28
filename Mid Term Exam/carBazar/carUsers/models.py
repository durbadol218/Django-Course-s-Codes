from django.db import models
from django.contrib.auth.models import User
from cars.models import CarModel
# Create your models here.
class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)