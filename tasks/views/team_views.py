from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from tasks.models import Team


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team
    paginate_by = 5


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("tasks:team-list")


class TeamUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("tasks:team-list")


class TeamDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("tasks:team-list")
