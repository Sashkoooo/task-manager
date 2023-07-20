from django.test import TestCase
from tasks.models import Position, Worker, TaskType, Task


class PositionModelTestCase(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Manager")

    def test_str_method(self):
        self.assertEqual(str(self.position), "Manager")


class WorkerModelTestCase(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Manager")
        self.worker = Worker.objects.create(
            first_name="John",
            last_name="Doe",
            position=self.position
        )

    def test_str_method(self):
        expected_str = "John Doe, position: Manager"
        self.assertEqual(str(self.worker), expected_str)


class TaskTypeModelTestCase(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Feature")

    def test_str_method(self):
        self.assertEqual(str(self.task_type), "Feature")


class TaskModelTestCase(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Manager")
        self.worker = Worker.objects.create(
            first_name="John",
            last_name="Doe",
            position=self.position
        )
        self.task_type = TaskType.objects.create(name="Feature")
        self.task = Task.objects.create(
            name="Task 1",
            description="Description for Task 1",
            deadline="2023-07-20 12:00:00",
            priority="High",
            type=self.task_type,
            created_by=self.worker,
            updated_by=self.worker,
        )
        self.task.assignees.add(self.worker)

    def test_str_method(self):
        expected_str = "Task 1"
        self.assertEqual(str(self.task), expected_str)
