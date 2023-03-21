from django.contrib import admin

from timetable.models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ("tags", "deadline", "created")


admin.site.register(Tag)
