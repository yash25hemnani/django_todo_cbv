from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task_create/', TaskCreate.as_view(), name='task_create'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('task_update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task_delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
]