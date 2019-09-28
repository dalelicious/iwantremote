from django.urls import path

from . import views

app_name = 'resources'

urlpatterns = [
	path('resources/', views.blog, name='blog')
]