from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

from .models import Task

# Create your views here.


class IndexView(generic.ListView):
    template_name = "taskr_app/index.html"
    context_object_name = "tasks_due_soon_list"

    def get_queryset(self):
        return Task.objects.filter(complete__exact="False").order_by("due_next")


class DetailView(generic.DetailView):
    model = Task
    template_name = "taskr_app/detail.html"
    context_object_name = "task_detail"

    # def get_queryset(self, pkid):
    #     return Task.objects.filter(id=pkid)
