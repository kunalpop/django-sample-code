from django.db import models

class City(models.Model):
    unloc_code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100, null=True, blank=True)
    timezone = models.CharField(max_length=50,null=True)
    alias = models.JSONField(default=list)
    regions = models.JSONField(default=list)
    coordinates_lat = models.FloatField(null=True, blank=True)
    coordinates_lon = models.FloatField(null=True, blank=True)
    code = models.CharField(max_length=10,null=True)

    def __str__(self):
        return f"{self.name} ({self.unloc_code})"
    
    class Meta: 
        verbose_name_plural = "Cities"

