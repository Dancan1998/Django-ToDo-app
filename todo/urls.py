from django.urls import path
from .views import TaskListView, TastDetailView
app_name = 'todo'

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>', TastDetailView.as_view(), name='task-detail'),
]
