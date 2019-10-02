# Django
from django.db import models

from company.models import Company

# Create your models here.
class Jobs(models.Model):

	company = models.CharField(max_length=50, null=True)
	title = models.CharField(max_length=50, null=True)
	category = models.IntegerField(null=True)
	job_type = models.CharField(max_length=50, null=True)
	headquarters = models.CharField(max_length=50, null=True)
	region = models.CharField(max_length=50, null=True)
	link = models.CharField(max_length=50, null=True)
	description = models.CharField(max_length=200, null=True)
	create_date = models.DateTimeField()
	is_featured = models.BooleanField(null=True)
	is_active = models.BooleanField(null=True)


	@property
	def get_job_company(self):

		company = Company.objects.get(email=self.company)

		return company.logo


	@property
	def get_company_name(self):

		company = Company.objects.get(email=self.company)

		return company.name