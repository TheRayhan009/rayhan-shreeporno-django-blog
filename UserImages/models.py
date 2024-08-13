from django.db import models

# Create your models here.

class UPImage(models.Model):
    UPimage = models.ImageField(upload_to='images')
    UPtitel=models.CharField(max_length=500)
    Pdate=models.DateField(auto_now_add=True)
    PUimage=models.ImageField()
    PUname=models.CharField(max_length=30)