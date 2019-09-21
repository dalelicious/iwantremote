from django.db import models

# Create your models here.
class Jobs(models.Model):

	job_title = models.CharField(max_length=50, null=True)
	category = models.CharField(max_length=50, null=True)
	job_type = models.CharField(max_length=50, null=True)
	headquarters = models.CharField(max_length=50, null=True)
	region = models.CharField(max_length=50, null=True)
	apply_link = models.CharField(max_length=50, null=True)
	job_description = models.CharField(max_length=50, null=True)