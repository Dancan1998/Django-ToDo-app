from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Task
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'


class TastDetailView(DetailView):
    model = Task
    context_object_name = 'task_detail'


class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo:task-list')
