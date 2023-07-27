from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.timezone import now

from tasks.models import Task


@login_required
def index(request):
    """View function for the home page of the site."""
    tasks = Task.objects.all()
    num_tasks = tasks.count()
    completed_tasks = tasks.filter(is_completed=True).count()
    in_progress_tasks = tasks.filter(is_completed=False).count()
    overdue_tasks = (
        tasks.filter(is_completed=False, deadline__lt=now().isoformat()).count()
    )

    context = {
        "num_tasks": num_tasks,
        "completed_tasks": completed_tasks,
        "in_progress_tasks": in_progress_tasks,
        "overdue_tasks": overdue_tasks,
    }

    return render(request, "tasks/index.html", context=context)
