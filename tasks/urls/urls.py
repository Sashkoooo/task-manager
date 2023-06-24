from django.urls import path, include

from tasks.views.index_views import index

urlpatterns = [
    path("", index, name="index"),
    path("positions/", include("tasks.urls.position_urls")),
    path("workers/", include("tasks.urls.worker_urls")),
    path("task-types/", include("tasks.urls.task_type_urls")),
    path("tasks/", include("tasks.urls.task_urls")),
    path("teams/", include("tasks.urls.team_urls")),
    path("projects/", include("tasks.urls.project_urls")),
]

app_name = "tasks"
