from django.shortcuts import render,redirect
from . import forms
from . import models

def add_task(request):
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.TaskForm()
    return render(request, 'add_task.html', {'form':form})


def edit_task(request, id):
    task = models.TaskModel.objects.get(pk=id)
    form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        form =forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'add_task.html', {'form':form})


def delete_task(request, id):
    task = models.TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('homepage')