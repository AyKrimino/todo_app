from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def display_tasks(request):
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('display-tasks')
    
    tasks = Task.objects.all()
    
    return render(request, 'todo/list_display.html', {
        'tasks': tasks,
        'form': form,
    })
