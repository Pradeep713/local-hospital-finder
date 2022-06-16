from django.contrib.auth.models import User
from django.db import models

class District(models.Model):
    districtName = models.CharField(max_length=32)
    def __str__(self):
        return self.districtName

class Mandal(models.Model):
    districtName = models.ForeignKey(District, on_delete=models.CASCADE)
    mandalName = models.CharField(max_length=64)
    def __str__(self):
        return self.mandalName

class City(models.Model):
    mandalName = models.ForeignKey(Mandal, on_delete=models.CASCADE)
    cityName = models.CharField(max_length=64)
    def __str__(self):
        return self.cityName

class Hospital(models.Model):
    districtName = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    mandalName = models.ForeignKey(Mandal, on_delete=models.SET_NULL, null=True)
    cityName = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    hospitalName = models.CharField(max_length=256)

    class Meta:
        ordering = ['-hospitalName']
    
    def __str__(self) -> str:
        return self.hospitalName[:50]