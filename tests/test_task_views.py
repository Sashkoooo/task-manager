from django.test import TestCase
from django.urls import reverse
from tasks.forms import TaskSearchForm
from tests.test_utils import setUpTestData
from tasks.models import Worker

TASKS_LIST = reverse("tasks:task-list")


class PublicTaskViewListTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        setUpTestData()

    def test_login_required(self):
        response = self.client.get(TASKS_LIST)
        self.assertNotEqual(response.status_code, 200)


class PrivateTaskListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        setUpTestData()

    def setUp(self) -> None:
        user = Worker.objects.get(username="johndoe")
        self.client.force_login(user)

    def test_retrieve_tasks(self):
        response = self.client.get(TASKS_LIST)
        self.assertEqual(response.status_code, 200)

        self.assertTrue(
            "page_obj" in response.context,
            "Pagination info not found in response"
        )
        page_obj = response.context["page_obj"]

        expected_items_per_page = 5
        self.assertEqual(len(page_obj.object_list), expected_items_per_page,
                         f"Expected {expected_items_per_page} tasks per page")

        expected_total_tasks = 38
        self.assertEqual(page_obj.paginator.count, expected_total_tasks,
                         f"Expected {expected_total_tasks} total tasks")
        self.assertTemplateUsed(response, "tasks/task/task_list.html")

    def test_task_list_view_search(self):
        """
        Search for task with name "Task 2 for John"
        Verify that the search form is present in the context
        """
        form_data = {
            "name": "Task 2 for John",
        }
        response = self.client.get(reverse("tasks:task-list"), data=form_data)
        self.assertEqual(response.status_code, 200)

        form = response.context["search_form"]
        self.assertIsInstance(form, TaskSearchForm)

        task_list = response.context["task_list"]
        self.assertEqual(len(task_list), 1)
        self.assertEqual(task_list[0].name, "Task 2 for John")
