from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class TeamListView(LoginRequiredMixin, generic.ListView):
    pass


class TeamDetailView(LoginRequiredMixin, generic.ListView):
    pass


class TeamCreateView(LoginRequiredMixin, generic.ListView):
    pass


class TeamUpdateView(LoginRequiredMixin, generic.ListView):
    pass


class TeamDeleteView(LoginRequiredMixin, generic.ListView):
    pass
