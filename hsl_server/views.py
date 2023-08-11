from django.http import HttpResponse
import requests


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def fetch_vehicle_position(request):
    response = requests.get("https://realtime.hsl.fi/realtime/vehicle-positions/v2/hsl")
    return HttpResponse(response)


def fetch_service_alert(request):
    response = requests.get("https://realtime.hsl.fi/realtime/service-alerts/v2/hsl")
    return HttpResponse(response)


def fetch_trip_updates(request):
    response = requests.get("https://realtime.hsl.fi/realtime/trip-updates/v2/hsl")
    return HttpResponse(response)
