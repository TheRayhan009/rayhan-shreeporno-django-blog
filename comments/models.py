from django.db import models

# Create your models here.


class Comment(models.Model):
    PURname=models.CharField(max_length=100,default=None,null=True)
    Ucomment=models.TextField(max_length=5000)
    UPBslug=models.CharField(max_length=500)
    Ucomment_image=models.ImageField(upload_to="comment/",max_length=100,null=True,default=None)
    UPdate=models.DateField(auto_now_add=True ,null=True)