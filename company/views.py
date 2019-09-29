# Django
from django.http 			import HttpResponse
from django.shortcuts 		import render
from django.shortcuts 		import redirect

# iwantremote
from . viewmodels 			import CompanyViewModel
from jobs.viewmodels 		import JobsViewModel
from category.viewmodels 	import CategoryViewModel


job = JobsViewModel()
company = CompanyViewModel()
category = CategoryViewModel()


def companies(request):

	all_jobs = len(job.get_jobs_list())
	company_list = company.get_company_list()
	category_list = category.get_category_list()

	return render(request, 'company/company.html',
				 {'all_jobs':all_jobs,
				  'company_list':company_list,
				  'category_list':category_list})


def company_detail(request, companyId):

	all_jobs = len(job.get_jobs_list())
	company_detail = company.get_company_by_id(companyId)
	job_posted = company.get_all_job_posted(companyId)
	category_list = category.get_category_list()

	return render(request, 'company/company_detail.html',
				 {'all_jobs':all_jobs,
				  'company':company_detail,
				  'job_posted':job_posted,
				  'category_list':category_list})


