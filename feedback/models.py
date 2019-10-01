from django.db import models

# Create your models here.
class Feedback(models.Model):

	name = models.CharField(max_length=50, null=True)
	content = models.CharField(max_length=200, null=True)
	create_date = models.DateTimeField()