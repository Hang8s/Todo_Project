from django.db import models

# Create your models here.
class TaskModel(models.Model):
    class Priority(models.TextChoices):
        LOW = 'low','low'
        MEDIUM = 'medium','medium'
        HIGHT = 'hight','hight'
    title = models.CharField(max_length=64)
    completed = models.BooleanField(default=False, blank=True)
    priority = models.CharField(max_length=10,choices=Priority.choices)
    body = models.TextField(blank=True,null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_edited = models.DateTimeField(auto_now=True)
    