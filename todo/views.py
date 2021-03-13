from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'


class TastDetailView(DetailView):
    model = Task
    context_object_name = 'task_detail'
