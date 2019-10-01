# Django
from django.db 		import models

# iwantremote
# from jobs.models 	import Jobs


# Create your models here.
class Company(models.Model):

	name = models.CharField(max_length=50, null=True)
	email = models.CharField(max_length=50, null=True)
	logo = models.ImageField(upload_to='images/companies/')
	tagline = models.CharField(max_length=50, null=True)
	website = models.CharField(max_length=50, null=True)
	description = models.CharField(max_length=200, null=True)


	# @property
	# def job_posted(self):

	# 	job_posted = len(Jobs.objects.filter(company=self.email))

	# 	return job_posted