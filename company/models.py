# Django
from django.db 		import models


# Create your models here.
class Company(models.Model):

	name = models.CharField(max_length=50, null=True)
	slugName = models.CharField(max_length=50, null=True)
	email = models.CharField(max_length=50, null=True)
	logo = models.ImageField(upload_to='images/companies/')
	tagline = models.CharField(max_length=50, null=True)
	website = models.CharField(max_length=50, null=True)
	description = models.TextField(null=True)
