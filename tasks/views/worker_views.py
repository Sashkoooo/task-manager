from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views import generic

from tasks.models import Worker


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "tasks/worker/worker_list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.exclude(is_superuser=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        for worker in context["object_list"]:
            worker.completed_tasks_count = (
                worker.tasks.filter(is_completed=True).count()
            )
            worker.tasks_in_progress_count = (
                worker.tasks.filter(is_completed=False).count()
            )
            worker.overdue_tasks_count = (
                worker.tasks.filter(is_completed=False, deadline__lt=now).count()
            )
        return context


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "tasks/worker/worker_detail.html"
    model = Worker

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        worker = self.object
        worker.completed_tasks_list = worker.tasks.filter(is_completed=True)
        worker.tasks_in_progress_list = worker.tasks.filter(is_completed=False)
        return context
