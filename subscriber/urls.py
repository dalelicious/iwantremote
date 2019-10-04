from django.urls import path

from . import views

app_name = 'subscriber'

urlpatterns = [
	path('sub_confirmation/', views.confirmation, name='sub_confirmation'),
	path('add_subscriber/', views.add_subscriber, name='add-subscriber')
]