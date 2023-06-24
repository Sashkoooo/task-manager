from django.urls import path
from tasks.views.worker_views import (
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
)

urlpatterns = [
    path("", WorkerListView.as_view(), name="worker-list"),
    path("<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("create/", WorkerCreateView.as_view(), name="worker-create"),
    path("<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
]
