from django.db import models

# Create your models here.
class Resources(models.Model):

	title = models.CharField(max_length=50, null=True)
	author = models.CharField(max_length=50, null=True)
	content = models.CharField(max_length=50, null=True)
	create_date = models.DateTimeField()
	blog_image = models.ImageField(upload_to='images/resources/')