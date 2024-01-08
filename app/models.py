from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.
class reg(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.IntegerField()
    conformpassword=models.IntegerField()
    areyou=models.CharField(max_length=50)
    
    def __str__(self):
        return self.firstname
class venuedetail(models.Model):
    image = models.ImageField(upload_to="media/")
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    price =models.IntegerField()
    
    def __str__(self):
        return self.name
class cakedetail(models.Model):
    image = models.ImageField(upload_to="media/")
    cakename= models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    price =models.IntegerField()
    
    def __str__(self):
        return self.cakename
class photographerdetail(models.Model):
    image = models.ImageField(upload_to="media/")
    photographername = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    price =models.IntegerField()
    
    def __str__(self):
        return self.photographername
class beautisiondetail(models.Model):
    b_image=models.ImageField(upload_to="media/")
    b_name=models.CharField(max_length=50)
    bcity=models.CharField(max_length=50)
    b_price=models.IntegerField()
    
    def __str__(self):
        return self.b_name
    