from django.db import models

# Create your models here.

class Profile(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	phone = models.CharField(max_length=255)
	summary = models.TextField(max_length=4000)
	university = models.CharField(max_length=255)
	school = models.CharField(max_length=255)
	work_experience = models.TextField(max_length=4000)

	def __str__(self):
		return self.name 
