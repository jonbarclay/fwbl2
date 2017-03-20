from django.db import models

# Create your models here.
class ip_address(models.Model):
    ip = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')