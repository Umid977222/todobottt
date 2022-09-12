from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions, renderers
from .models import Task
from .permissions import IsOwnerOrReadOnly
from .serializer import TaskSerializer
# Create your views here.
""" /listoftask
 /addtask = create task = post
 /removetask = delete
 /updatetask  = put
 /donetask = Task.objects.filter(completed == TRUE)
 /upcommingtask = Task.objects.filter(completed == FALSE)
 """


class TaskViewSet(viewsets.ModelViewSet):
    """get_all  and post functions"""
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=False)
    def completed(self, request):
        """function get_all to convert the data in the database to json format"""
        if request.method == 'GET':
            result = Task.objects.filter(completed=True)
            serializer = TaskSerializer(result, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False)
    def uncompleted(self, request):
        """function get_all to convert the data in the database to json format"""
        if request.method == 'GET':
            result = Task.objects.filter(completed=False)
            serializer = TaskSerializer(result, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)




