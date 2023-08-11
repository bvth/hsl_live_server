from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("vehicle-positions", views.fetch_vehicle_position),
    path("service-alerts", views.fetch_service_alert),
    path("trip-updates", views.fetch_trip_updates)
]