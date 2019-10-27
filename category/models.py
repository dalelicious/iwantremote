from django.db import models

from jobs.models import Jobs

# Create your models here.
class Category(models.Model):

	name = models.CharField(max_length=50, null=True)
	slugCatName = models.CharField(max_length=50, null=True)
	cat_image = models.ImageField(upload_to='images/categories/')

	@property
	def jobs_per_category(self):

		jobs_per_category = Jobs.objects.filter(category=self.slugCatName, is_active=True).order_by('-create_date')[:15]

		return jobs_per_category


	@property
	def total_jobs_per_category(self):

		total_jobs_per_category = len(Jobs.objects.filter(category=self.slugCatName, is_active=True))

		return total_jobs_per_category