from django.urls import path, include

from tasks.views.index_views import index

urlpatterns = [
    path("", index, name="index"),
    path("workers/", include("tasks.urls.worker_urls")),
    path("tasks/", include("tasks.urls.task_urls")),
]

app_name = "tasks"
