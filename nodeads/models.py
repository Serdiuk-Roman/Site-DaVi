from django.db import models

class Culeba(models.Model):
    name = models.CharField(max_length=50)
    lon = models.FloatField()
    lat = models.FloatField()

    date = models.CharField(max_length=140)
    time = models.CharField(max_length=140)

    temp_max = models.FloatField()
    temp_min = models.FloatField()

    wind = models.FloatField()
    cloud = models.IntegerField()
    pressure = models.FloatField()
    description = models.CharField(max_length=140)

    def __str__(self):
        return str(self.date) + str(' ') + str(self.time)
