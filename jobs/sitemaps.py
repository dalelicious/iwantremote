from django.contrib.sitemaps import Sitemap
from jobs.models import Jobs

class PostSitemap(Sitemap):

	def items(self):
		return Jobs.objects.all()