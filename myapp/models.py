from email.policy import default
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    detail = models.CharField(max_length=1000, blank=True)
    target_amount = models.IntegerField(null=True)
    one_amount = models.IntegerField(null=True)
    n = models.IntegerField(default=0)
    d_day = models.DateTimeField(default=timezone.datetime.now)
    created_at = models.DateTimeField(default=timezone.datetime.now)