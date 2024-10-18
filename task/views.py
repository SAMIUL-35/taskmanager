from django.shortcuts import render, redirect, get_object_or_404
from .taskForm import TaskForm  
from .models import TaskModel

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_task')  
    else:
        form = TaskForm()
    return render(request, 'task.html', {'form': form})

def show_task(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_task.html', {'tasks': tasks})

def edit_task(request, id):
    
    task = get_object_or_404(TaskModel, pk=id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_task')  
    else:
        form = TaskForm(instance=task)
    return render(request, 'task.html', {'form': form})

def delete_task(request, id):
    task = get_object_or_404(TaskModel, pk=id)
    
    task.delete()
    return redirect('show_task')
    
