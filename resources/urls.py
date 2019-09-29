from django.urls import path

from . import views

app_name = 'resources'

urlpatterns = [
	path('blog/', views.blog, name='blog'),
	path('blog_detail/<int:blogId>/', views.blog_detail, name='blog-detail'),
	path('privacy/', views.privacy, name='privacy')
]