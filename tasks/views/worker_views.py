from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class WorkerListView(LoginRequiredMixin, generic.ListView):
    pass


class WorkerDetailView(LoginRequiredMixin, generic.ListView):
    pass


class WorkerCreateView(LoginRequiredMixin, generic.ListView):
    pass


class WorkerUpdateView(LoginRequiredMixin, generic.ListView):
    pass


class WorkerDeleteView(LoginRequiredMixin, generic.ListView):
    pass
