from django.db import models
from django.contrib.auth.models import User

# FLAGS
class Flag(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=100)
    points = models.IntegerField()