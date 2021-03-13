from django.urls import path
from .views import TaskListView, TastDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, CustomLoginView, RegisterView
from django.contrib.auth.views import LogoutView
app_name = 'todo'

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='todo:login'), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>', TastDetailView.as_view(), name='task-detail'),
    path('task-create', TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDeleteView.as_view(), name='task-delete'),
]
