from django.contrib import admin
from .models import Task, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # @staticmethod
    # def status_ordering(task):
    #     status_order = {
    #         'pending': 1,
    #         'in progress': 2,
    #         'completed': 3
    #     }
    #
    #     return status_order[task.status]

    list_display = ['title', 'created', 'priority', 'status', 'assigned_user']
    list_filter = ['created', 'priority', 'status', 'assigned_user', 'categories']
    search_fields = ['title', 'assigned_user']
    ordering = ['priority', '-created', 'status']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']