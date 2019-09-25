from django.urls import path

from . import views

app_name = 'category'

urlpatterns = [
    path('categories/', views.categories, name='categories')
]