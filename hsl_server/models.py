from django.db import models

# Create your models here.
class ServiceAlert(models.Model):
    headerText = models.CharField(max_length=255)
    descriptionText = models.CharField(max_length=255)
    entityId = models.CharField(max_length=10)