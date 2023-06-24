from django.urls import path
from tasks.views.position_views import (
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
)

urlpatterns = [
    path("", PositionListView.as_view(), name="position-list"),
    path("create/", PositionCreateView.as_view(), name="position-create"),
    path("<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
]
