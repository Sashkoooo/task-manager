from django.test import TestCase
from tasks.forms import TaskForm
from tasks.models import Worker, Task, TaskType
from tests.test_utils import setUpTestData


class TaskFormTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        setUpTestData()

    def setUp(self) -> None:
        user = Worker.objects.get(username="johndoe")
        self.client.force_login(user)

        self.task_type = TaskType.objects.create(name="Low")
        self.worker1 = Worker.objects.get(first_name="Worker 1")
        self.worker2 = Worker.objects.get(first_name="Worker 2")

        self.form_data = {
            "name": "Task 3 for John",
            "description": "Task 3 description",
            "deadline": "2023-07-31T12:00:00Z",
            "completed": False,
            "priority": "Urgent",
            "type": self.task_type.pk,
            "assignees": [self.worker1, self.worker2],
        }
        self.form = TaskForm(data=self.form_data)

    def test_task_form_valid_data(self):
        self.assertTrue(self.form.is_valid())

    def test_task_form_save(self):
        task = self.form.save()
        self.assertIsInstance(task, Task)

    def test_car_form_invalid_data(self):
        """Provide invalid data (missing task type instance)"""
        form_data = {
            "name": "Task 4 for John",
            "description": "Task 3 description",
            "deadline": "2023-07-31T12:00:00Z",
            "completed": False,
            "priority": "Urgent",
            "type": "",
            "assignees": [self.worker1, self.worker2],
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
