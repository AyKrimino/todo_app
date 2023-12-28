from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = {
        'pending': 'pending',
        'completed': 'completed',
        'in progress': 'in progress',
    }

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='pending')
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True, null=True)

    def __str__(self):
        return self.title
