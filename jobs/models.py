import re

# Django
from django.db import models

from company.models import Company

# sitemaps

from django.urls import reverse

# Create your models here.
class Jobs(models.Model):

	company = models.CharField(max_length=50, null=True)
	title = models.CharField(max_length=50, null=True)
	slugTitle = models.CharField(max_length=50, null=True)
	category = models.CharField(max_length=50, null=True)
	job_type = models.CharField(max_length=50, null=True)
	salary = models.CharField(max_length=50, null=True)
	tags = models.CharField(max_length=50, null=True)
	headquarters = models.CharField(max_length=50, null=True)
	region = models.CharField(max_length=50, null=True)
	link = models.CharField(max_length=50, null=True)
	description = models.TextField(null=True)
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


	@property
	def get_job_tags(self):

		job_tags = self.tags
		tags_list = re.sub("[^\w]", " ", job_tags).split()

		return tags_list


	def get_absolute_url(self):
		return reverse('post', args=[str(self.slugTitle)])