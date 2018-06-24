from django.db import models

# Create your models here.
class form(models.Model):
    title=models.CharField(max_length=500)
    content=models.TextField(max_length=5000,blank=True)
    file = models.FileField(blank=True)

class document(models.Model):
    title=models.CharField(max_length=500)
    url=models.CharField(max_length=500,blank=True)
    file = models.FileField(blank=True)

class EngDocument(models.Model):
    title=models.CharField(max_length=500)
    url=models.CharField(max_length=500,blank=True)
    file = models.FileField(blank=True)
