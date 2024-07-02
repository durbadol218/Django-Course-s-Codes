from django.db import models
from category.models import TaskCategory
# Create your models here.

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    TaskAssignDate = models.DateField(auto_now_add=True)
    
    # Relations
    categories = models.ManyToManyField(TaskCategory)
    def __str__(self):
        return f"{self.taskTitle}"