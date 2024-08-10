from django.db import models

# Create your models here.
class Users(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    user_name=models.CharField(max_length=40,unique=True)
    password=models.CharField(max_length=30)
    USER_image=models.ImageField(upload_to="user/",max_length=150,default=None,null=True)