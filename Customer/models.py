from django.db import models
from Agent.models import Customer,Product
# Create your models here.


class Customer_order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			) 
	Payment_Opetion = (
			('CBE', 'CBE'),
			('TellBirr', 'TellBirr'),
		
			) 
	Customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete= models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	Payment_Opetion =models.CharField(max_length=200, null=True, choices=Payment_Opetion)
	
