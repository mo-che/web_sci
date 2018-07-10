from django.db import models

# Create your models here.

class reg(models.Model):
    title = models.CharField(max_length=500)
    date=models.DateField()
    content = models.TextField(max_length=5000,null=True,blank=True)
    link = models.URLField(max_length=500, null=True)
    file = models.FileField(upload_to='files/',blank=True)
    def __str__(self):
        return self.title