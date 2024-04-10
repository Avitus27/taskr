from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from taskr_app.models import Task

# Create your views here.


def get(request, pk):
    task = get_object_or_404(Task, id=pk)
    # return JsonResponse({task}, safe=False)
    # return JsonResponse({"foo": "bar"})
    res = {
        "title": task.title,
        "description": task.description,
        "assigned_to": task.assigned_to.username,
        "due_next": task.due_next,
        "is_overdue": task.is_overdue(),
        "is_repeating": task.repeats,
    }
    if not task.repeats:
        res["complete"] = task.complete
    return JsonResponse(res)


def complete(request, pk):
    task = get_object_or_404(Task, id=pk)
    res = task.mark_done()
    task.save()
    if res[0]:
        if res[1]:
            return JsonResponse({"success": True, "complete": True})
        else:
            return JsonResponse({"success": True, "complete": False, "due_next": task.due_next})
    else:
        return JsonResponse({"success": False})
