from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Task
from .forms import TaskForm


def display_tasks(request):
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = Task(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                assigned_user=User.objects.get(username='admin'),
            )
            new_task.save()
            for category in form.cleaned_data['categories']:
                new_task.categories.add(category)
        return redirect('display-tasks')
    
    tasks = Task.objects.all()
    
    return render(request, 'todo/list_display.html', {
        'tasks': tasks,
        'form': form,
    })
