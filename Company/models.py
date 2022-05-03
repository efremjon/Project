from operator import mod
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Admin(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    Full_Name=models.CharField(max_length=300, null=True)
    phone1 = models.CharField(max_length=200, null=True)
    phone2 = models.CharField(max_length=200, null=True)
    facebook = models.CharField(max_length=200, null=True,blank=True)
    telegram = models.CharField(max_length=200, null=True,blank=True)
    instagram = models.CharField(max_length=200, null=True,blank=True)
    about = models.TextField(max_length=500, null=True)
    profile_pic=models.ImageField(null=True,blank=True, upload_to='Profile/')
    Company = models.CharField(max_length=200, null=True)
    Job = models.CharField(max_length=200, null=True)
    Country = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.user)
    
class Region(models.Model):
	Region_Name=models.CharField(max_length=100,blank=True, null=True)
	def __str__(self) -> str:
		return self.Region_Name

class Rgeion_Manager(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
   
    Region=models.OneToOneField(Region,null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200, null=True)
    Adderes = models.CharField(max_length=200, null=True)
    about=models.TextField(null=True,blank=True,max_length=500)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    Telegram = models.CharField(max_length=200, null=True)
    facebook = models.CharField(max_length=200, null=True)
    instagrm = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.user.first_name

class Stor(models.Model):
    Stor_Name = models.CharField(max_length=200, null=True)
    Location = models.CharField(max_length=200, null=True)

class Stor_Manager(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    Stor=models.OneToOneField(Stor,null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200, null=True)
    Adderes = models.CharField(max_length=200, null=True)
    about=models.TextField(null=True,blank=True,max_length=500)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    Telegram = models.CharField(max_length=200, null=True)
    facebook = models.CharField(max_length=200, null=True)
    instagrm = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.user.first_name
    
class Product(models.Model):
    Stor=models.OneToOneField(Stor,null=True, on_delete=models.CASCADE)
    product_Name=models.CharField(max_length=200, null=True)
    product_Quintitiy=models.CharField(max_length=200, null=True)
class Product_Price(models.Model):
    Product=models.OneToOneField(Product,null=True, on_delete=models.CASCADE)
    Price=models.FloatField()

class Agent(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    Full_Name=models.CharField(max_length=300, null=True)
    phone1 = models.CharField(max_length=200, null=True)
    phone2 = models.CharField(max_length=200, null=True)
    facebook = models.CharField(max_length=200, null=True)
    telegram = models.CharField(max_length=200, null=True)
    instagram = models.CharField(max_length=200, null=True)
    about = models.TextField(max_length=500, null=True)
    profile_pic=models.ImageField(null=True,blank=True, upload_to='Profile/')
    city = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=500, null=True)
    TIN_NO = models.CharField(max_length=500, null=True)
    License = models.FileField(null=True, blank=True, upload_to='License')
    agreement = models.FileField(null=True, blank=True, upload_to='Agreement')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.user)
    
    
class Advertisment(models.Model):
    auther=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    data=models.TextField(null=True,blank=True,max_length=500)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
class Finace_Manager(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200, null=True)
    Adderes = models.CharField(max_length=200, null=True)
    about=models.TextField(null=True,blank=True,max_length=500)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    Telegram = models.CharField(max_length=200, null=True)
    facebook = models.CharField(max_length=200, null=True)
    instagrm = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.user.first_name