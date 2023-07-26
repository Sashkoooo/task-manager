from django.test import TestCase
from django.urls import reverse

from tasks.models import Worker
from tests.test_utils import setUpTestData


class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        setUpTestData()

    def setUp(self) -> None:
        user = Worker.objects.get(username="johndoe")
        self.client.force_login(user)
        self.overdue_tasks = 555

    def test_index_view(self):
        response = self.client.get(reverse("tasks:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/index.html")
