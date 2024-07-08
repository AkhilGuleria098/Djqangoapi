# tasks/urls.py
from django.urls import path
from.views import UserListView, UserDetailView, TaskListView, TaskDetailView

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('tasks/', TaskListView.as_view()),
]