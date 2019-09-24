# Django
from django.http 			import HttpResponse
from django.shortcuts 		import render
from django.shortcuts 		import redirect

# iwantremote
from . viewmodels 			import CompanyViewModel


company = CompanyViewModel()


def company_detail(request, companyId):

	company_detail = company.get_company_by_id(companyId)
	job_posted = company.get_all_job_posted(companyId)

	return render(request, 'company/company_detail.html',
				 {'company' : company_detail,
				  'job_posted' : job_posted})


