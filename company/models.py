# Django
from django.db 		import models

from django.urls import reverse


# Create your models here.
class Company(models.Model):

	name = models.CharField(max_length=50, null=True)
	slugName = models.CharField(max_length=50, null=True)
	email = models.CharField(max_length=50, null=True)
	logo = models.ImageField(upload_to='images/companies/')
	tagline = models.CharField(max_length=50, null=True)
	website = models.CharField(max_length=50, null=True)
	description = models.TextField(null=True)

<<<<<<< HEAD
=======

	@property
	def total_job_posted(self):

		from jobs.models import Jobs

		total_jobs = len(Jobs.objects.filter(company=self.email))

		return total_jobs

>>>>>>> 04266d39df4e2cde91d71d35fd0f7f0a9962c9ae
