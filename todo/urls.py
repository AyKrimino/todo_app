from django.urls import path
from . import views


urlpatterns = [
    path('', views.display_tasks, name='display-tasks'),
    path('create-task/', views.create_task, name='create-task'),
    path('update-task/<int:task_id>/', views.update_task, name='update-task'),

]

htmx_urlpatterns = [
    path('check_task_title/', views.check_task_title, name='check-task-title'),
]

urlpatterns += htmx_urlpatterns