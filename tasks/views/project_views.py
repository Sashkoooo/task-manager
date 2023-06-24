from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class ProjectListView(LoginRequiredMixin, generic.ListView):
    pass


class ProjectDetailView(LoginRequiredMixin, generic.ListView):
    pass


class ProjectCreateView(LoginRequiredMixin, generic.ListView):
    pass


class ProjectUpdateView(LoginRequiredMixin, generic.ListView):
    pass


class ProjectDeleteView(LoginRequiredMixin, generic.ListView):
    pass
