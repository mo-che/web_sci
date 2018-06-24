from django.db import models

# Create your models here.
class meetingTable(models.Model):
    month=models.CharField(max_length=100)
    date=models.CharField(max_length=50)
    dueDate=models.CharField(max_length=200)

class report(models.Model):
    title= models.CharField(max_length=200)
    file = models.FileField(blank=True)
    date=models.DateTimeField(null=True)
