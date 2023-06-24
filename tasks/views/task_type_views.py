from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    pass


class TaskTypeCreateView(LoginRequiredMixin, generic.ListView):
    pass


class TaskTypeUpdateView(LoginRequiredMixin, generic.ListView):
    pass


class TaskTypeDeleteView(LoginRequiredMixin, generic.ListView):
    pass
