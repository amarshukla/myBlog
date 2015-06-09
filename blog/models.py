from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.user')
	title = models.CharField(max_length = 200)
	content = models.TextField()
	created_date = models.DateTimeField(null=True)
	publish_date = models.DateTimeField(null=True)

def publish(self):
        self.published_date = timezone.now()
        self.save()

def __str__(self):
    return self.title