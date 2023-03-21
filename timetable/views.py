from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from timetable.models import Tag, Task


# Create your views here.
class TagListViews(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "timetable/tag_list.html"
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "timetable/tag_form.html"
    success_url = reverse_lazy("timetable:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "timetable/tag_form.html"
    success_url = reverse_lazy("timetable:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    template_name = "timetable/tag_confirm_delete.html"
    success_url = reverse_lazy("timetable:tag-delete")


class TaskListViews(generic.ListView):
    model = Tag
    context_object_name = "task_list"
    template_name = "timetable/task_list.html"
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "timetable/task_form.html"
    success_url = reverse_lazy("timetable:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "timetable/task_form.html"
    success_url = reverse_lazy("timetable:task-list")


class TaskUpdateCompletionView(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        task.is_completed = not task.is_completed
        task.save()

        return redirect("timetable:task-list")

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.is_completed = request.POST.get("is_completed", not task.is_completed)
        task.save()
        return redirect("timetable:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    template_name = "timetable/task_confirm_delete.html"
    success_url = reverse_lazy("timetable:task-delete")
