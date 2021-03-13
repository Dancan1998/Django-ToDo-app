from django.urls import path
from .views import TaskListView, TastDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
app_name = 'todo'

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>', TastDetailView.as_view(), name='task-detail'),
    path('task-create', TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDeleteView.as_view(), name='task-delete'),
]
