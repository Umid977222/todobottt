# from django.urls import path
# from .views import TaskList, TaskDetail
#
# urlpatterns = [
#     path('tasks/', TaskList.as_view()),
#     path('task/<int:pk>', TaskDetail.as_view()),
# ]
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='todobotapp')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework'))
]
