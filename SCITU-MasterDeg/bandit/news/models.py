from django.db import models

# Create your models here.
class public(models.Model):
    title = models.CharField(max_length=500)
    date=models.DateField()
    content = models.TextField(max_length=5000)
    file = models.FileField(blank=True)


class fund(models.Model):
    title = models.CharField(max_length=500)
    date=models.DateField()
    content = models.TextField(max_length=5000)
    file = models.FileField(blank=True)
