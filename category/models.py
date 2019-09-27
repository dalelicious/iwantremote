from django.db import models

from jobs.models import Jobs

# Create your models here.
class Category(models.Model):

	name = models.CharField(max_length=50, null=True)
	cat_image = models.ImageField(upload_to='images/categories/')

	@property
	def jobs_per_category(self):

		jobs_per_category = Jobs.objects.filter(category=self.id).order_by('-id')[:3][::-1]

		return jobs_per_category