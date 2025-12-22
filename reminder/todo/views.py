from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from .models import Task
from django.urls import reverse

class TaskListView(ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'create.html'
    fields = '__all__'
    success_url = '/todo/'

class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/todo/'

class TaskDetailView(UpdateView):
    model = Task
    context_object_name = 'task'
    fields = ['done']
    template_name = 'details.html'

    def get_success_url(self):
        return reverse("details", kwargs={"pk": self.object.pk})