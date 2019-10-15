from django.urls import path

from . import views

app_name = 'company'

urlpatterns = [
	path('companies/', 							views.companies, 		name='companies'),
    path('company/<slug:companyName>', 	views.company_detail, 	name='company-detail')
]