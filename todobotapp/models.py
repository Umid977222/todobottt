from django.db import models

# Create your models here.


class Task(models.Model):
    task_name = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    completed = models.BooleanField()
    starting_time = models.DateTimeField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.task_name}'

# def upload_location(filename):
#   output = filename.split.('.')[-1]
#   return f'{filename}{datetime.now()}.{output}'

# class Fileupload(models.Model):
#   img = models.ImageField(upload_to=upload_location)
