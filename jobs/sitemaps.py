from django.contrib.sitemaps import Sitemap
from . models import Jobs
from django.urls import reverse

class JobSitemap(Sitemap):
	changefreq = "hourly"
	priority = 1.0

	def items(self):
		return Jobs.objects.all().order_by('id')

	def lastmod(self, obj):
		return obj.create_date

class StaticSitemap(Sitemap):

    def items(self):
        return [
            'company:companies',
            'subscriber:add-subscriber',
            'subscriber:sub_confirmation',
            'resources:blog',
            'resources:privacy',
            'resources:job_template',
            'feedback:feedback',
            'jobs:jobs',
            'jobs:create-job'
        ]

    def location(self, item):
        return reverse(item)