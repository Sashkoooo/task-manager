from django.urls import path
from tasks.views.team_views import (
    TeamCreateView,
    TeamDeleteView,
    TeamDetailView,
    TeamListView,
    TeamUpdateView
)

urlpatterns = [
    path("", TeamListView.as_view(), name="team-list"),
    path("<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
    path("create/", TeamCreateView.as_view(), name="team-create"),
    path("<int:pk>/update/", TeamUpdateView.as_view(), name="team-update"),
    path("<int:pk>/delete/", TeamDeleteView.as_view(), name="team-delete"),
]
