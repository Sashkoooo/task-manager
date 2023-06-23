from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasks.models import (
    Worker,
    Position,
    TaskType,
    Task,
    Team,
    Project
)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    pass


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
