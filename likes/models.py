from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Likes(models.Model):
    UserName=models.CharField(max_length=500)
    A_likeSlug=models.CharField(max_length=500,default=None,null=True)