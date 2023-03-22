from datetime import datetime

from django.test import TestCase
from django.urls import reverse

import pytz
from timetable.models import Task, Tag


TASK_URL = reverse("timetable:task-list")
TAG_URL = reverse("timetable:tag-list")


class PrivateTaskTest(TestCase):
    def setUp(self) -> None:
        europe_kiev = pytz.timezone('Europe/Kiev')
        self.task = Task.objects.create(
            content="Test",
            deadline=datetime(2024, 3, 12, 11, 30, tzinfo=europe_kiev),
            is_completed=False
        )
        self.url = reverse("timetable:update-completion", kwargs={'pk': self.task.pk})

    def test_retrieve_tasks(self):
        europe_kiev = pytz.timezone('Europe/Kiev')
        Task.objects.create(
            content="Test",
            deadline=datetime(2024, 3, 12, 11, 30, tzinfo=europe_kiev),
        )

        response = self.client.get(TASK_URL)

        tasks = Task.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks)
        )

        self.assertTemplateUsed(response, "timetable/task_list.html")

    def test_for_update_task_completion(self):
        # Initial check if task is not completed
        self.assertFalse(self.task.is_completed)

        # Testing if task is marked as completed if it wasn't
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 302)

        self.task.refresh_from_db()
        self.assertTrue(self.task.is_completed)

        # Check for "Undo" button to make task not completed
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 302)

        self.task.refresh_from_db()
        self.assertFalse(self.task.is_completed)


class PrivateTagTest(TestCase):
    def test_retrieve_tags(self):
        Tag.objects.create(name="Home")
        Tag.objects.create(name="School")

        response = self.client.get(TAG_URL)

        tags = Tag.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["tag_list"]),
            list(tags)
        )

        self.assertTemplateUsed(response, "timetable/tag_list.html")
