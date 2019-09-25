from django.urls import path

from . import views

app_name = 'company'

urlpatterns = [
	path('companies/', 							views.companies, 		name='companies'),
    path('company_detail/<int:companyId>/', 	views.company_detail, 	name='company-detail')
]