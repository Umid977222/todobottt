import datetime
from django.contrib.auth import login
from knox.models import AuthToken
from rest_framework import permissions, generics
from knox.views import LoginView as KnoxLoginView
from django.utils import timezone
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions, renderers
from .models import Task
from .serializer import TaskSerializer, RegisterSerializer, UserSerializer, LoginUserSerializer

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
        tasks = Task.objects.filter(completed=True)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False)
    def uncompleted(self, request):
        tasks = Task.objects.filter(completed=False)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False)
    def daily(self, request):
        if Task.objects.filter(completed=False):
            task = Task.objects.filter(deadline__gte=timezone.now().today())
            serializer = TaskSerializer(task, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class RegistrationAPI(generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = LoginUserSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    # @action(detail=True)
    # def change(self, request, pk):
    #     result = Task.objects.get(pk=pk)
    #     serializer = TaskSerializer(result, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status.HTTP_304_NOT_MODIFIED)

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
