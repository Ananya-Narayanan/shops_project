from django.db import models

# Create your models here.

class contactdb(models.Model):
    Firstname=models.CharField(max_length=20,null=True,blank=True)
    Lastname=models.CharField(max_length=20,null=True,blank=True)
    Email=models.CharField(max_length=20,null=True,blank=True)
    Address=models.CharField(max_length=20,null=True,blank=True)
    City=models.CharField(max_length=20,null=True,blank=True)
    Country=models.CharField(max_length=20,null=True,blank=True)
    message=models.CharField(max_length=20,null=True,blank=True)

class registerdb(models.Model):
    Name=models.CharField(max_length=20,null=True,blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email=models.CharField(max_length=20,null=True,blank=True)
    Username = models.CharField(max_length=20, null=True, blank=True)
    Password=models.CharField(max_length=20,null=True,blank=True)

class cartdb(models.Model):
    username=models.CharField(max_length=20,null=True,blank=True)
    productname=models.CharField(max_length=20,null=True,blank=True)
    description=models.CharField(max_length=20,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    Totalprice=models.IntegerField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)




