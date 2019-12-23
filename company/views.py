# Django
from django.http 			import HttpResponse
from django.shortcuts 		import render, get_object_or_404
from django.shortcuts 		import redirect
from django.core.paginator 	import Paginator

# iwantremote
from . viewmodels 			import CompanyViewModel
from jobs.viewmodels 		import JobsViewModel
from category.viewmodels 	import CategoryViewModel

# sitemaps
from . models import Company

job = JobsViewModel()
company = CompanyViewModel()
category = CategoryViewModel()


def companies(request):

	if request.method == "GET":

		all_jobs = len(job.get_jobs_list())
		company_list = company.get_company_list()
		category_list = category.get_category_list()

		page = request.GET.get('page', 1)
		paginator = Paginator(company_list, 20)

		try:
			company_list = paginator.page(page)
		except PageNotAnInteger:
			company_list = paginator.page(1)
		except EmptyPage:
			company_list = paginator.page(paginator.num_pages)

		return render(request, 'company/company.html',
					 {'all_jobs':all_jobs,
					  'company_list':company_list,
					  'category_list':category_list})

	else:

		search = request.POST['search']

		all_jobs = len(job.get_jobs_list())
		company_list = company.get_company_result_list(search)
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
	company_headquarters = company.get_company_headquarters(companyName)

	return render(request, 'company/company_detail.html',
				 {'all_jobs':all_jobs,
				  'company':company_detail,
				  'job_posted':job_posted,
				  'job_posted_by_company':job_posted_by_company,
				  'category_list':category_list,
				  'company_headquarters':company_headquarters})




