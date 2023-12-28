from django.contrib import admin
from .models import Task, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'status', 'assigned_user']
    list_filter = ['created', 'status', 'assigned_user', 'categories']
    search_fields = ['title', 'assigned_user', 'categories']
    ordering = ['-status', '-created']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']