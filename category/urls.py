from django.urls import path

from . import views

app_name = 'category'

urlpatterns = [
    path('categories/<slug:categoryName>/', 		views.categories, 		name='categories')
]