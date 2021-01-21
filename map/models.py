from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import datetime


class Coordinates(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return (self.x,self.y)
