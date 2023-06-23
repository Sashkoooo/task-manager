from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}, position: {self.position}"


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("Urgent", "Urgent priority rate"),
        ("High", "High priority rate"),
        ("Middle", "Middle priority rate"),
        ("Low", "Low priority rate")
    )

    task_name = models.CharField(max_length=255)
    task_description = models.TextField()
    task_deadline = models.DateTimeField()
    task_is_completed = models.BooleanField(default=False)
    task_priority = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES,
    )
    task_type = models.ForeignKey(to=TaskType, on_delete=models.CASCADE)
    task_assignees = models.ManyToManyField(Worker, related_name="tasks")
    task_created_at = models.DateTimeField(auto_now_add=True)
    task_updated_at = models.DateTimeField(auto_now=True)
    task_created_by = models.ForeignKey(
        Worker,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_tasks"
    )
    task_updated_by = models.ForeignKey(
        Worker,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_tasks"
    )

    class Meta:
        ordering = ["task_name"]

    def __str__(self):
        return self.task_name


class Team(models.Model):
    name = models.CharField(max_length=255)
    teammates = models.ManyToManyField(to=Worker, related_name="teams")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    project_team = models.ForeignKey(to=Team, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
