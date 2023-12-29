from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from django.contrib.auth.models import User

from .models import Task
from .forms import TaskForm


def display_tasks(request):
    
    
    tasks = Task.objects.all()
    
    return render(request, 'todo/display_tasks.html', {
        'tasks': tasks,
        
    })
    

def create_task(request):
    
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
    
    form = TaskForm()

    return render(request, 'todo/create_task.html', {
        'form': form,
        
    })


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
                
        return redirect('display-tasks')
    
    form = TaskForm(instance=task)
    
    return render(request, 'todo/update_task.html', {
        'form': form,
        
    })
    

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    return render(request, 'todo/task_detail.html', {
        'task': task,
        
    }) 
    

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect('display-tasks')
    
    return render(request, 'todo/delete_task.html', {
        'task': task,
        
    })


# htmx views to handle frontend events
def check_task_title(request):
    title = request.POST.get('title')
    if Task.objects.filter(title=title).exists():
        return HttpResponse('<div id="title-errors" style="color: red;">This title already exists</div>')
    return HttpResponse('<div id="title-errors" style="color: green;">This is a valid title</div>')
