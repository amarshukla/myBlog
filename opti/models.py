from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class User(models.Model):
    f_name = models.CharField(max_length=200)