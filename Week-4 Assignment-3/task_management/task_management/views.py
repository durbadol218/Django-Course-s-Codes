from django.shortcuts import render
from task.models import TaskModel

def homepage(request):
    data = TaskModel.objects.all()
    return render(request, 'home.html', {'tasks': data})