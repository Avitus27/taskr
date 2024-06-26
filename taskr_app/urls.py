from django.urls import path, include

from . import views

app_name = "taskr_app"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>", views.DetailView.as_view(), name="detail")
]
