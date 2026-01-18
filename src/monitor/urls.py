from django.urls import path
from . import views

urlpatterns = [
    path("", views.monitor_sala, name="monitor_sala"),
]
