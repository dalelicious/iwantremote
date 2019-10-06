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


def company_detail(request, companyName):

	all_jobs = len(job.get_jobs_list())
	company_detail = company.get_company_by_name(companyName)
	job_posted = len(company.get_all_job_posted(companyName))
	job_posted_by_company = company.get_all_job_posted(companyName)
	category_list = category.get_category_list()

	return render(request, 'company/company_detail.html',
				 {'all_jobs':all_jobs,
				  'company':company_detail,
				  'job_posted':job_posted,
				  'job_posted_by_company':job_posted_by_company,
				  'category_list':category_list})


