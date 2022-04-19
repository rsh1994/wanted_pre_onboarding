from email.policy import default
from django.db import models
from django.utils import timezone

# Create your models here.
class Goods(models.Model):
    title = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    detail = models.CharField(max_length=1000, blank=True)
    target_amount = models.IntegerField(null=False)
    one_amount = models.IntegerField(null=False)
    d_day = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.datetime.now)

    funding_rate = models.IntegerField(null=True)
    total_amount = models.IntegerField(null=True)
    n = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title