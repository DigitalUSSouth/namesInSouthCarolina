from django.db import models
from .model_settings import ModelSettings as settings
class Region(models.Model):
    name = models.CharField(max_length=settings.name_limit,
                            null=False, blank=False)

    def __str__(self):
        return "Region: {}".format(self.name)
