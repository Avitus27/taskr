from django.urls import path, include

from . import views

app_name = "api"

urlpatterns = [
    path("get/<int:pk>", views.get, name="get_by_id"),
    path('complete/<int:pk>', views.complete, name="complete_task"),
]
