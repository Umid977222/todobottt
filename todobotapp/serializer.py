from rest_framework.serializers import ModelSerializer
from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_name', 'description', 'completed', 'starting_time', 'deadline']
