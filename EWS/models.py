from datetime import datetime
from django.db import models


class Area(models.Model):
    area_code = models.CharField(max_length=50, default='')
    area_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'area'

class Hazard(models.Model):
    id = models.AutoField(primary_key=True)
    hazard_name = models.CharField(max_length=50, default='')

    class Meta:
        db_table = 'hazard'


class HazardReading(models.Model):
    id = models.AutoField(primary_key=True)
    hazard = models.ForeignKey(Hazard)
    reading = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    reading_date = models.DateField(auto_now_add=True, default=datetime.now())
    extent_image_file = models.CharField(max_length=255, default='')
    vulnerability_image_file = models.CharField(max_length=255, default='')
    risk_image_file = models.CharField(max_length=255, default='')
    threshold_level = models.CharField(max_length=50, default='')

    class Meta:
        db_table = 'hazard_reading'
