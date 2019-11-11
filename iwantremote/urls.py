# Django
from django.conf 				import settings
from django.urls 				import path
from django.urls 				import include
from django.contrib 			import admin
from django.conf.urls.static 	import static
from django.views.generic import TemplateView

# Sitemap
from django.contrib.sitemaps.views import sitemap
from jobs.sitemaps import JobSitemap, StaticSitemap
from jobs import views

sitemaps = {
	'jobs' : JobSitemap,
	'static': StaticSitemap,
}

urlpatterns = [
	path('',            include('jobs.urls')),
	path('', 			include('company.urls')),
	path('', 			include('category.urls')),
	path('', 			include('feedback.urls')),
	path('', 			include('resources.urls')),
	path('', 			include('subscriber.urls')),
	path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
		name='django.contrib.sitemaps.views.sitemap'),
	path('remote-jobs/<slug:jobName>/', views.post, name='jobpost'),
	path('admin/',      admin.site.urls),
	path('robots.txt', TemplateView.as_view(template_name="jobs/robots.txt", content_type='text/plain')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

