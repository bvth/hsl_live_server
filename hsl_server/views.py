import json

import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from hsl_server.models import ServiceAlert


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def fetch_vehicle_position(request):
    response = requests.get("https://realtime.hsl.fi/realtime/vehicle-positions/v2/hsl")
    return HttpResponse(response)


@csrf_exempt
def fetch_service_alert(request):
    if request.method == "GET":
        response = requests.get("https://realtime.hsl.fi/realtime/service-alerts/v2/hsl")
        return HttpResponse(response)
    if request.method == "POST":
        json_data = json.loads(request.body)
        alert = ServiceAlert(headerText_en=json_data["headerText_en"],
                             descriptionText_en=json_data["descriptionText_en"],
                             entityId=json_data["entityId"],
                             start=json_data["start"],
                             end=json_data["end"])
        alert.save()
        return HttpResponse("Done")

def fetch_trip_updates(request):
    response = requests.get("https://realtime.hsl.fi/realtime/trip-updates/v2/hsl")
    return HttpResponse(response)
