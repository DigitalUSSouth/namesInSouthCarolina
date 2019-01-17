from django.db import models
from .model_settings import ModelSettings as settings

class County(models.Model):
    name = models.CharField(max_length=settings.name_limit,
                            null=False, blank=False)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)

    def __str__(self):
        return "County: {}, Region: {}".format(self.name, self.region.name)
