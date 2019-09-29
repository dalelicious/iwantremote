# Django
from django.http 			import HttpResponse
from django.shortcuts 		import render
from django.shortcuts 		import redirect

# iwantremote
from . viewmodels 			import JobsViewModel
from company.viewmodels 	import CompanyViewModel
from category.viewmodels 	import CategoryViewModel


job = JobsViewModel()
company = CompanyViewModel()
categories = CategoryViewModel()


def jobs(request):

	all_jobs = len(job.get_jobs_list())
	jobs_list = job.get_featured_jobs_list()
	total_featured_jobs = len(jobs_list)
	category_list = categories.get_category_list()

	return render(request, 'jobs/jobs.html',
				 {'all_jobs':all_jobs,
				  'jobs_list':jobs_list,
				  'total_featured_jobs':total_featured_jobs,
				  'category_list':category_list})


def create_job(request):

	if request.method == "GET":

		all_jobs = len(job.get_jobs_list())
		category_list = categories.get_category_list()

		return render(request, 'jobs/create_jobs.html',
					 {'all_jobs':all_jobs,
					  'category_list':category_list})

	else:

		title = request.POST['title']
		category = request.POST['category']
		job_type = request.POST['job_type']
		headquarters = request.POST['headquarters']
		region = request.POST['region']
		link = request.POST['link']
		job_description = request.POST['job_description']
		if 'featured' in request.POST:
			is_featured = request.POST['featured']
		else:
			is_featured = False

		print(is_featured)

		name = request.POST['company_name']
		logo = request.FILES['logo']
		tagline = request.POST['tagline']
		website = request.POST['website']
		email = request.POST['email']
		company_description = request.POST['company_description']

		job.create_new_job(email, title, category, job_type, headquarters, region, link, job_description, is_featured)

		company.create_new_company(name, logo, tagline, website, email, company_description)

		return redirect('jobs:jobs')


def job_detail(request, jobId):

	job_detail = job.get_job_id(jobId)
	all_jobs = len(job.get_jobs_list())
	category_list = categories.get_category_list()
	company_detail = company.get_company_by_job_id(jobId)

	return render(request, 'jobs/job_detail.html',
				 {'job':job_detail,
				  'all_jobs':all_jobs,
				  'company':company_detail,
				  'category_list':category_list})


