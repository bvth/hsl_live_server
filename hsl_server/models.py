from django.db import models


# Create your models here.
class ServiceAlert(models.Model):
    headerText_en = models.CharField(max_length=255)
    descriptionText_en = models.CharField(max_length=255)
    entityId = models.CharField(max_length=50)
    start = models.CharField(max_length=255)
    end = models.CharField(max_length=255)
