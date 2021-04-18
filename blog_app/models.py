from django.db import models
# Create your models here.


class Blog(models.Model):
    titile = models.CharField(max_length=50)
    time = models.TimeField(auto_now=True)
    body = models.TextField()
    by = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
