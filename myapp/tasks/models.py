# tasks/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)

    # Specify a related_name argument for the many-to-many relationships
    groups = models.ManyToManyField(Group, related_name='tasks_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='tasks_permissions', blank=True)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)