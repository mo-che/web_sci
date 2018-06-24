from django.db import models

# Create your models here.

class reg(models.Model):
    title = models.CharField(max_length=500)
    date=models.DateField()
    content = models.TextField(max_length=5000)
    file = models.FileField(blank=True)
