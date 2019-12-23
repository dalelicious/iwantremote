from django.urls import path

from . import views

app_name = 'resources'

urlpatterns = [
	path('blog/', 							views.blog, 		name='blog'),
	path('blog_detail/<slug:blogTitle>/', 	views.blog_detail, 	name='blog-detail'),
	path('privacy/', 						views.privacy, 		name='privacy'),
	path('job_template/', 					views.job_template, name='job_template'),
	path('testimony/', 						views.testimony, 	name='testimony'),
	path('howitworks/', 					views.howitworks, 	name='howitworks'),
]