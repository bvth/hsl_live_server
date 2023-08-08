from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("vehicle-positions", views.fetch_vehicle_position)
]