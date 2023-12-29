from django.urls import path
from . import views


urlpatterns = [
    path('', views.display_tasks, name='display-tasks'),
    path('create-task/', views.create_task, name='create-task'),
    path('update-task/<int:task_id>/', views.update_task, name='update-task'),
    path('task-detail/<int:task_id>/', views.task_detail, name='task-detail'),
    path('task_delete/<int:task_id>/', views.task_delete, name='task-delete'),

]

htmx_urlpatterns = [
    path('check_task_title/', views.check_task_title, name='check-task-title'),

]

urlpatterns += htmx_urlpatterns