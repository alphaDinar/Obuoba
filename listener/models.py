from django.db import models

class Time(models.Model):
    cur = models.TimeField(default='08:00')
    