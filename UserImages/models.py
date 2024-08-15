from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class UPImage(models.Model):
    UPimage = models.ImageField(upload_to='images')
    UPtitel=models.CharField(max_length=500)
    Pdate=models.DateField(auto_now_add=True)
    Plikes=models.IntegerField(default=0,null=True)
    Pdislikes=models.IntegerField(default=0,null=True)
    PUimage=models.ImageField()
    PUname=models.CharField(max_length=30)
    
    A_imageSlug=AutoSlugField(populate_from='UPtitel',unique=True,null=True,default=None)