from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class TaskListView(LoginRequiredMixin, generic.ListView):
    pass


class TaskDetailView(LoginRequiredMixin, generic.ListView):
    pass


class TaskCreateView(LoginRequiredMixin, generic.ListView):
    pass


class TaskUpdateView(LoginRequiredMixin, generic.ListView):
    pass


class TaskDeleteView(LoginRequiredMixin, generic.ListView):
    pass
