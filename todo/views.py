from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todo:task-list')


class RegisterView(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todo:task-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todo:task-list')
        return super(RegisterView, self).get(*args, **kwargs)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context


class TastDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task_detail'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('todo:task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('todo:task-list')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task_delete'
    success_url = reverse_lazy('todo:task-list')
