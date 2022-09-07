from django.db import models

# Create your models here.


class Task(models.Model):
    task_name = models.CharField(max_length=200, blank=True )
    description = models.TextField()
    completed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)


