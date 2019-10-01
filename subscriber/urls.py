from django.urls import path

from . import views

app_name = 'subscriber'

urlpatterns = [
	path('add_subscriber/', views.add_subscriber, name='add-subscriber')
]