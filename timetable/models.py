from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(null=True, default=True)
    tags = models.ManyToManyField(Tag, related_name="tags")

    def __str__(self) -> str:
        return self.content
