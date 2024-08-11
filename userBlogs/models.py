from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class UBlog(models.Model):
    Utitel=models.CharField(max_length=50)
    Upost_blog=models.TextField(max_length=5000)
    Upost_image=models.ImageField(upload_to="blog/",max_length=100,null=True,default=None)
    Udate_of_post=models.DateField()
    Upost_category=models.CharField(max_length=30)
    Uproimage=models.ImageField(upload_to="user/",max_length=100,null=True,default=None)
    Uname=models.CharField(max_length=100)
    UFname = models.CharField(max_length=100,default=None,null=True)
    
    A_slugUserBlog=AutoSlugField(populate_from='Utitel',unique=True,null=True,default=None)
    