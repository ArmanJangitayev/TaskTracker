from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Task(models.Model):
    TODO = 'To Do'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'
    STATUS_CHOICES = (
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    dead_line = models.DateField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='To Do')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    media = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.title
