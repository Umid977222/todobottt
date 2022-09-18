from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions, renderers
from .models import Task
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False)
    def completed(self, request):
        """function get_all to convert the data in the database to json format"""
        if request.method == 'GET':
            tasks = Task.objects.filter(completed=True)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False)
    def uncompleted(self, request):
        if request.method == 'GET':
            tasks = Task.objects.filter(completed=False)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True)
    def deletetask(self, request, pk):
        if request.method == 'GET':
            task = Task.objects.filter(pk=pk)
            task.delete()
            return Response(status=status.HTTP_200_OK)

    # @action(detail=True)
    # def edit(self, request, pk):
    #     if request.method == 'GET':
    #         task = Task.objects.filter(pk=pk)
    #         serializer = TaskSerializer(task, many=True)
    #         task.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         """"""
#         serializer = TaskSerializer(request=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
#
#
# class TaskDetail(APIView):
#     """put and delete functions"""
#     def get_object(self, pk):
#         task: Task = Task.objects.get(pk)
#         try:
#             return task
#         except Task.DoesNotExist:
#             raise status.HTTP_400_BAD_REQUEST
#
#     def completed(self, request):
#         result = Task.objects.filter(completed=True)
#
#     def get(self, request, pk, format=None):
#         task = self.get_object(pk)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         result = self.get_object(pk)
#         serializer = TaskSerializer(result, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         task = self.get_oject(pk)
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
