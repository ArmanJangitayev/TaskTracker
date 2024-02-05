from django.urls import path

from Task.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TasksViewAPI, TasksViewDetailAPI

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete'),
    path('api/', TasksViewAPI.as_view(), name='api'),
    path('api/<int:pk>/', TasksViewDetailAPI.as_view(), name='api_detail')
]