from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Register(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=255)
    username=models.CharField(max_length=200)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    phone=models.CharField(max_length=255)
    role=models.CharField(max_length=100)
    password=models.CharField(max_length=255)
    confirm_password=models.CharField(max_length=255)

    def __str__(self):
        return self.first_name


class Products(models.Model):
    product_name=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    price=models.IntegerField()
    description=models.CharField(max_length=255)
    product_image=models.ImageField(null=True,blank=True,upload_to="images/")



    def __str__(self):
        return self.product_name

