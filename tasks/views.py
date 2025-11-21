from django.views.generic import ListView, DetailView, CreateView
from .models import Task, Category
from .forms import TaskForm
from django.db.models import Q

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().select_related('category')
        q = self.request.GET.get('q', '').strip()
        category = self.request.GET.get('category', '')
        if q:
            qs = qs.filter(title__icontains=q)
        if category:
            qs = qs.filter(category__id=category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_category'] = self.request.GET.get('category', '')
        context['q'] = self.request.GET.get('q', '')
        return context

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
