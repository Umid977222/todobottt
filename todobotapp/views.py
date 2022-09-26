from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from .models import Task
from .serializer import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """get_all  and post functions"""
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False)
    def completed(self, request):
        """function get_all to convert the data in the database to json format"""
        tasks = Task.objects.filter(completed=True)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False)
    def uncompleted(self, request):
        tasks = Task.objects.filter(completed=False)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def task1(self, request, pk):
    #     tasks = Task.objects.get(pk=pk)
    #     serializer = TaskSerializer(tasks)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # @action(detail=False)
    # def get_object(self, pk):
    #     try:
    #         return Task.objects.get(pk=pk)
    #     except Task.DoesNotExist:
    #         raise status.HTTP_404_NOT_FOUND
    #
    # def get(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = TaskSerializer(snippet)
    #     return Response(serializer.data)
    # @action(detail=False)
    # def get_one1(self, request, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     task = get_object_or_404(Task, pk=pk)
    #     serializer = TaskSerializer(task)
    #     return Response(serializer.data)

    # @action(detail=True)
    # def delete(self, request, pk):
    #     if request.method == 'GET':
    #         task = Task.objects.filter(pk=pk)
    #         task.delete()
    #         return Response(status=status.HTTP_200_OK)

    # def change(self, request, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     save_allowance = get_object_or_404(Task.objects.all(), pk=pk)
    #     data = request.data.get('task_name')
    #     serializer = TaskSerializer(instance=save_allowance, data=data, partial=True)
    #
    #     if serializer.is_valid():
    #         allowance_saved = serializer.save()
    #         return Response({"success": "Allowance '{}' updated successfully".format(allowance_saved.AllowID)})
    #     else:
    #         return Response({"fail": "'{}'".format(serializer.errors)})

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
#         task = self.get(pk)
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
