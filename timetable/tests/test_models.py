from datetime import datetime

from django.test import TestCase

from timetable.models import Tag, Task


class ModelTest(TestCase):
    def test_task_format_str(self):
        task = Task.objects.create(
            content="Test",
            deadline=datetime(2024, 3, 12, 11, 30)
        )
        self.assertEqual(
            str(task),
            f"{task.content}"
        )

    def test_tag_str(self):
        tag = Tag.objects.create(name="Test")
        self.assertEqual(
            str(tag),
            f"{tag.name}"
        )
