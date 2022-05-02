from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Root(models.Model):
	Root_No=models.IntegerField()
	City=models.CharField(max_length=2002,null=True)
	Kebel=models.CharField(max_length=200,null=True)
	def __str__(self) -> str:
		return self.City + "|" + "Root_No."  + str(self.Root_No)

class Customer(models.Model):
	user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
	Compan_name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	Adderes = models.CharField(max_length=200, null=True)	
	about=models.TextField(null=True,blank=True,max_length=500)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	Rooting=models.OneToOneField(Root,null=True, on_delete=models.CASCADE)
	Telegram = models.CharField(max_length=200, null=True)
	facebook = models.CharField(max_length=200, null=True)
	instagrm = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.user.first_name
