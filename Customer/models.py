from django.db import models
from Agent.models import Customer,Product_in_Agent_Stor
from Company.models import Product
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
  Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
  #product = models.ForeignKey(Product_in_Agent_Stor, on_delete= models.SET_NULL, null=True)
 
  total_payment=models.FloatField(default=0.0,null=True,blank=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  status = models.CharField(max_length=200, null=True, choices=STATUS)
  Payment_Option =models.CharField(max_length=200, null=True, choices=Payment_Opetion)


products=Product.objects.all()
for product in products:
    Customer_order.add_to_class(product.Product_Name,models.IntegerField(default=0))  