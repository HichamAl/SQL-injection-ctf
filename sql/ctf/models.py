from django.db import models
from django.contrib.auth.models import User

# FLAGS
class Flag(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=100)
    points = models.IntegerField()

# classified data
class Classified(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=100)
    points = models.IntegerField()

# Encryption method
class Encryption(models.Model):
    mode = models.CharField(max_length=100)
    key_size_in_bits = models.CharField(max_length=100)
    Initialization_vector = models.CharField(max_length=100)
    secret_key = models.CharField(max_length=100)
