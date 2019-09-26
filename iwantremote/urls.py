# Django
from django.conf 				import settings
from django.urls 				import path
from django.urls 				import include
from django.contrib 			import admin
from django.conf.urls.static 	import static


urlpatterns = [
	path('',            include('jobs.urls')),
	path('', 			include('company.urls')),
	path('', 			include('category.urls')),
	path('admin/',      admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
