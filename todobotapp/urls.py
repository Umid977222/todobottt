# from django.urls import path
# from .views import TaskList, TaskDetail
#
# urlpatterns = [
#     path('tasks/', TaskList.as_view()),
#     path('task/<int:pk>', TaskDetail.as_view()),
# ]
from knox import views as knox_views
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
# router.register(r'login', views.LoginView, name='knox_login')
# router.register(r'logout/', knox_views.LogoutView, basename='knox_logout')
# router.register(r'logoutall/', knox_views.LogoutAllView, basename='knox_logoutall')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework')),
    path('register/', views.RegistrationAPI.as_view()),
    # path('login/', views.LoginAPI.as_view()),
    # path('user/', views.UserAPI.as_view()),
]
