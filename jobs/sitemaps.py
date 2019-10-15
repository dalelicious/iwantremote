from django.contrib.sitemaps import Sitemap
from . models import Jobs

class PostSitemap(Sitemap):
	changefreq = "hourly"
	priority = 1.0

	def items(self):
		return Jobs.objects.all().order_by

	def lastmod(self, obj):
		return obj.create_date