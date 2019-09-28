from django.urls import path

from . import views

app_name = 'resources'

urlpatterns = [
	path('blog/', views.blog, name='blog'),
	path('privacy/', views.privacy, name='privacy')
]