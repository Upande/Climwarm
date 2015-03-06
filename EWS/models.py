from django.db import models

class Area(models.Model):
	area_code = models.CharField(max_length=50, default='')
	area_name = models.CharField(max_length=50, null=False)

	class Meta:
		db_table = 'area'