from pickle import FALSE
from django.db import models
from django.contrib.auth.models import User
from Company.models import Agent,Product
# Create your models here.
class Route(models.Model):
	Root_No=models.IntegerField()
	City=models.CharField(max_length=2002,null=True)
	Kebel=models.CharField(max_length=200,null=True)
	def __str__(self) -> str:
		return self.City + "|" + "Root_No."  + str(self.Root_No)

class Customer(models.Model):
	user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
	Compan_name = models.CharField(max_length=200, null=True)
	phone1 = models.CharField(max_length=200, null=True)
	phone2 = models.CharField(max_length=200, null=True)
	Adderes = models.CharField(max_length=200, null=True)
	profile_pic=models.ImageField(null=True,blank=True, upload_to='Profile/')	
	about=models.TextField(null=True,blank=True,max_length=500)
	Routing=models.OneToOneField(Route,null=True, on_delete=models.CASCADE)
	Telegram = models.CharField(max_length=200, null=True)
	facebook = models.CharField(max_length=200, null=True)
	instagrm = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	TIN_NO = models.CharField(max_length=500, null=True)
	License = models.FileField(null=True, blank=True, upload_to='License')
	agreement = models.FileField(null=True, blank=True, upload_to='Agreement')
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return self.user.first_name
		
class Agent_Store(models.Model):
    Store_Name = models.CharField(max_length=200, null=True)
    Location = models.CharField(max_length=200, null=True)
	
class Agent_Store_Manager(models.Model):
	user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
	Store=models.OneToOneField(Agent_Store,null=True, on_delete=models.CASCADE)
	Agent=models.OneToOneField(Agent,null=True, on_delete=models.CASCADE)
	phone1 = models.CharField(max_length=200, null=True)
	Adderes = models.CharField(max_length=200, null=True)
	about=models.TextField(null=True,blank=True,max_length=500)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	Telegram = models.CharField(max_length=200, null=True)
	facebook = models.CharField(max_length=200, null=True)
	instagrm = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.user.first_name

class Vehicle(models.Model):
	vichel_type = models.CharField(max_length=200, null=True)
	vichel_No = models.CharField(max_length=200, null=True)
	Agent=models.OneToOneField(Agent,null=True, on_delete=models.CASCADE)

class Driver(models.Model):
	user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
	Agent=models.OneToOneField(Agent,null=True, on_delete=models.CASCADE)
	Vichel=models.OneToOneField(Vehicle,null=True, on_delete=models.CASCADE)
	phone1 = models.CharField(max_length=200, null=True)
	Adderes = models.CharField(max_length=200, null=True)
	about=models.TextField(null=True,blank=True,max_length=500)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	Telegram = models.CharField(max_length=200, null=True)
	facebook = models.CharField(max_length=200, null=True)
	instagrm = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.user.first_name

class Agent_finance(models.Model):
	user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
	Agent=models.OneToOneField(Agent,null=True, on_delete=models.CASCADE)
	phone1 = models.CharField(max_length=200, null=True)
	Adderes = models.CharField(max_length=200, null=True)
	about=models.TextField(null=True,blank=True,max_length=500)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	Telegram = models.CharField(max_length=200, null=True)
	facebook = models.CharField(max_length=200, null=True)
	instagrm = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.user.first_name


class Product_in_Agent_Stor(models.Model):
	Product_Type = (
			('castel', 'castel'),
			('senq', 'senq'),
			('doppel', 'doppel'),
			('george', 'george'),
			) 

	Type = models.CharField(max_length=200, null=True, choices=Product_Type)
	Store=models.OneToOneField(Agent_Store,null=True, on_delete=models.CASCADE)
	price = models.FloatField(null=True) 
	Agent=models.OneToOneField(Agent,null=True, on_delete=models.CASCADE)
	quantity=models.IntegerField(null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.Type

class Agent_order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			) 
<<<<<<< HEAD
	
	Agent = models.ForeignKey(Agent, on_delete= models.SET_NULL, null=True)
	total_payment=models.FloatField(default=0.0,null=True,blank=True)

	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	paid = models.BooleanField(default=False)
	

products=Product.objects.all()
for product in products:
    Agent_order.add_to_class(product.Product_Name,models.IntegerField(default=0))  
=======
>>>>>>> c40150777447daa0217a7fc7443b2f52df083f9a
	

	Agent = models.ForeignKey(Agent, on_delete= models.SET_NULL, null=True)
	
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	def __str__(self) -> str:
		return str(self.Agent)
products=Product.objects.all()
for product in products:
	Agent_order.add_to_class(product.Product_Name,models.IntegerField(default=0))

