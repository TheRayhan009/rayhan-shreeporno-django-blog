from django.db import models
from autoslug import AutoSlugField


class Blogs(models.Model):
    titel=models.CharField(max_length=50)
    post_blog=models.TextField(max_length=5000)
    post_image=models.ImageField(upload_to="blog/",max_length=100,null=True,default=None)
    # short_blog=models.CharField(max_length=150)
    date_of_post=models.DateField()
    post_category=models.CharField(max_length=30)
    
    
    A_slug=AutoSlugField(populate_from='titel',unique=True,null=True,default=None)
    
