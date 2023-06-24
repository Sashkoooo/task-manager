from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class PositionListView(LoginRequiredMixin, generic.ListView):
    pass


class PositionCreateView(LoginRequiredMixin, generic.ListView):
    pass


class PositionUpdateView(LoginRequiredMixin, generic.ListView):
    pass


class PositionDeleteView(LoginRequiredMixin, generic.ListView):
    pass
