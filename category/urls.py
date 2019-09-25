from django.urls import path

from . import views

app_name = 'category'

urlpatterns = [
    path('categories/<int:categoryId>/', 		views.categories, 		name='categories')
]