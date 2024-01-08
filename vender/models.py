from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.
class regdetail(models.Model):
    username=models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    conformpassword=models.CharField(max_length=50)
    phonenumber = models.IntegerField()
    
    def __str__(self):
      return self.username
class coupledetail(models.Model):
  image=models.ImageField(upload_to='images')
  couplename=models.CharField(max_length=50)
  email=models.EmailField()
  phone=models.IntegerField()
  descriptions=models.TextField()
  
  def __str__(self):
    return self.couplename
  
class coupleguestdetail(models.Model):
  image=models.ImageField(upload_to="media/")
  name=models.CharField(max_length=50)
  city=models.CharField(max_length=50)
  price=models.IntegerField()
  
  def __str__(self):
    return self.name