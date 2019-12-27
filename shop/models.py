from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=255)
	price = models.FloatField()
	discounter_price = models.FloatField()
	category = models.CharField(max_length=255)
	description = models.TextField(max_length=1000)
	image = models.CharField(max_length=300)

	def __str__(self):
		return self.title