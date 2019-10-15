# Django
from django.conf 				import settings
from django.urls 				import path
from django.urls 				import include
from django.contrib 			import admin
from django.conf.urls.static 	import static

# Sitemap
from django.contrib.sitemaps.views import sitemap
from jobs.sitemaps import PostSitemap
from jobs import views as jobs_view


sitemaps = {
	'posts' : PostSitemap,
}

urlpatterns = [
	path('',            include('jobs.urls')),
	path('', 			include('company.urls')),
	path('', 			include('category.urls')),
	path('', 			include('feedback.urls')),
	path('', 			include('resources.urls')),
	path('', 			include('subscriber.urls')),
	path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
	path('remote-jobs/<slug:jobName>', jobs_view.post, name='post'),
	path('admin/',      admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

