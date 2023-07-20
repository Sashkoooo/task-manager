from django.urls import path
from tasks.views.worker_views import (
    WorkerListView,
    WorkerDetailView,
)

urlpatterns = [
    path("", WorkerListView.as_view(), name="worker-list"),
    path("<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
]
