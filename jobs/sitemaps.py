from django.contrib.sitemaps import Sitemap
from . models import Jobs

class PostSitemap(Sitemap):

	def items(self):
		return Jobs.objects.all().order_by('id')