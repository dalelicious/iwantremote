from django.contrib.sitemaps import Sitemap
from . models import Company

class CompanySitemap(Sitemap):
	changefreq = "hourly"
	priority = 1.0

	def items(self):
		return ['company']