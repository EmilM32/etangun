from django.db import models
import datetime


class LevelDict(models.Model):
    belt_level = models.CharField(max_length=10, blank=True)


class Members(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(default=datetime.datetime.now, blank=True)
    belt_level = models.ForeignKey(
        LevelDict, on_delete=models.CASCADE, blank=True
    )
    group = models.IntegerField()
    is_active = models.BooleanField(default=True)
    comment = models.TextField(blank=True)
