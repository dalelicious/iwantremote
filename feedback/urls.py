from django.urls import path

from . import views

app_name = 'feedback'

urlpatterns = [
	path('feedback/', views.feedback, name='feedback'),
	path('confirmation/', views.confirmation, name='confirmation'),
	path('create_feedback/', views.create_feedback, name='create-feedback')
]