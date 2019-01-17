from django.db import models

class PinPoint(models.Model):
    name = models.TextField(null=False, blank=False)
    lon = models.FloatField()
    lat = models.FloatField()
    soundfile = models.TextField(null=True, blank=True)
    county = models.ForeignKey('County', on_delete=models.CASCADE)

    def __str__(self):
        return "Point: {}, {}, {}".format\
                (self.name, self.county.name, self.county.region.name)
