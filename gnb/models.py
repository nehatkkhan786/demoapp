from django.db import models

# Create your models here.

class Customer(models.Model):
	firm_name = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	phone = models.IntegerField()

	def __str__(self):
		return self.firm_name

class Product(models.Model):
	name = models.CharField(max_length=266)
	size = models.CharField(max_length=255)
	price = models.IntegerField()

	def __str__(self):
		return self.name

		
class Damage(models.Model):
	firm_name = models.ForeignKey(Customer, on_delete = None, related_name='damage_firm_name')
	name = models.ForeignKey(Customer, on_delete = None, related_name='damage_customer_name')
	product = models.ForeignKey(Product, on_delete = None, related_name='damage_product')
	mfg = models.DateTimeField(auto_now=False, auto_now_add=False)
	expiry = models.DateTimeField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return str(self.product)
