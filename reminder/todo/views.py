from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
     model = Task
     template_name = 'details.html'
     context_object_name = 'task'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'create.html'
    fields = '__all__'


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'create.html'