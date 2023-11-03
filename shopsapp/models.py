from django.db import models

# Create your models here.
class catdb(models.Model):
    CategoryName=models.CharField(max_length=20,null=True,blank=True)
    Description=models.CharField(max_length=20,null=True,blank=True)
    Image=models.ImageField(upload_to="dp",null=True,blank=True)

class prodb(models.Model):
    CategoryName=models.CharField(max_length=20,null=True,blank=True)
    ProductName=models.CharField(max_length=20,null=True,blank=True)
    Description=models.CharField(max_length=20,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Image=models.ImageField(upload_to="dp",null=True,blank=True)




