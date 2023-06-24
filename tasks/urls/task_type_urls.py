from django.urls import path

from tasks.views.task_type_views import (
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeDeleteView,
    TaskTypeUpdateView,
)

urlpatterns = [
    path("", TaskTypeListView.as_view(), name="task-type-list"),
    path("create/", TaskTypeCreateView.as_view(), name="task-type-create"),
    path("<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task-type-update"),
    path("<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="task-type-delete"),
]
