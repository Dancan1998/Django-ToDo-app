from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todo:task-list')


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


class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo:task-list')


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task_delete'
    success_url = reverse_lazy('todo:task-list')
