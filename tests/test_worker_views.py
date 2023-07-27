from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from tests.test_utils import setUpTestData
from tasks.models import Worker

WORKER_LIST = reverse("tasks:worker-list")


class WorkerListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        setUpTestData()

    def setUp(self) -> None:
        """Login superuser to run tests"""
        self.client.login(
            username="superuser",
            password="superpassword"
        )
        self.response = self.client.get(WORKER_LIST)

    def test_worker_list_view_url_exists_at_desired_location(self):
        response = self.client.get("/tasks/workers/")
        self.assertEqual(response.status_code, 200)

    def test_worker_list_view_url_accessible_by_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_worker_list_view_uses_correct_template(self):
        self.assertTemplateUsed(self.response, "tasks/worker/worker_list.html")

    def test_worker_list_view_pagination_is_five(self):
        self.assertTrue("is_paginated" in self.response.context)
        self.assertTrue(self.response.context["is_paginated"] is True)
        self.assertTrue(len(self.response.context["worker_list"]) == 5)

    def test_worker_list_view_lists_all_workers(self):
        """
        Get third page and confirm it has remaining 3 items
        (not including superuser to test get_queryset()
        in WorkerListView)
        """
        response = self.client.get(reverse("tasks:worker-list") + "?page=3")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertTrue(len(response.context["worker_list"]) == 3)

    def test_worker_list_view_get_context_data(self):
        self.assertEqual(self.response.status_code, 200)
        context = self.response.context

        for worker in context["worker_list"]:
            completed_tasks_count = worker.tasks.filter(is_completed=True).count()
            tasks_in_progress_count = worker.tasks.filter(is_completed=False).count()
            now = timezone.now()
            overdue_tasks_count = (
                worker.tasks.filter(is_completed=False, deadline__lt=now).count()
            )

            self.assertEqual(worker.completed_tasks_count, completed_tasks_count)
            self.assertEqual(worker.tasks_in_progress_count, tasks_in_progress_count)
            self.assertEqual(worker.overdue_tasks_count, overdue_tasks_count)


class WorkerDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        setUpTestData()

    def test_worker_detail_view_get_context_data(self):
        self.client.login(username="superuser", password="superpassword")

        # Get the worker's ID for the URL
        worker = Worker.objects.get(username="johndoe")
        url = reverse("tasks:worker-detail", kwargs={"pk": worker.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Get the context from the response
        context = response.context

        # Check the tasks in the context based on their statuses
        worker = context["object"]
        completed_tasks_list = worker.tasks.filter(is_completed=True)
        tasks_in_progress_list = worker.tasks.filter(is_completed=False)

        self.assertEqual(
            list(worker.completed_tasks_list), list(completed_tasks_list)
        )

        self.assertEqual(
            list(worker.tasks_in_progress_list), list(tasks_in_progress_list)
        )
