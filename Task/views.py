from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from Task.models import Task
from Task.forms import TaskCreateForm, TaskUpdateForm
from Task.serializers import TaskSerializer


# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/list.html'

    def get_object(self, queryset=None):
        if queryset is not None:
            return queryset.objects.get(pk=self.kwargs['pk'])
        return None

    def get_queryset(self):
        queryset = super(TaskListView, self).get_queryset()
        search_query = self.request.GET.get('search', False)
        if search_query:
            queryset = queryset.filter(title__icontains=search_query, description__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        queryset = self.get_queryset()
        context['todo_tasks'] = queryset.filter(status=Task.TODO).all()

        context['in_progress_tasks'] = queryset.filter(status=Task.IN_PROGRESS).all()

        context['done_tasks'] = queryset.filter(status=Task.COMPLETED).all()
        return context


class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/create.html'
    form_class = TaskCreateForm
    queryset = Task.objects.all()

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tasks/update.html'
    form_class = TaskUpdateForm
    queryset = Task.objects.all()

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')


class TasksViewAPI(ListAPIView, CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TasksViewDetailAPI(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
