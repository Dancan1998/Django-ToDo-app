from django.urls import path
from .views import TaskListView, TastDetailView, TaskCreateView
app_name = 'todo'

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>', TastDetailView.as_view(), name='task-detail'),
    path('task-create', TaskCreateView.as_view(), name='task-create'),
]
