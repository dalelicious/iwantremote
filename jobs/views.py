# Django
from django.http 			import HttpResponse
from django.contrib 		import messages
from django.shortcuts 		import render
from django.shortcuts 		import redirect
from django.shortcuts 		import get_object_or_404

# iwantremote
from . viewmodels 			import JobsViewModel
from company.viewmodels 	import CompanyViewModel
from category.viewmodels 	import CategoryViewModel

# sitemaps
from . models import Jobs


job = JobsViewModel()
company = CompanyViewModel()
categories = CategoryViewModel()


def jobs(request):

	if request.method == "GET":

		all_jobs = len(job.get_jobs_list())
		jobs_list = job.get_featured_jobs_list()
		total_featured_jobs = len(jobs_list)
		category_list = categories.get_category_list()

		return render(request, 'jobs/jobs.html',
					 {'all_jobs':all_jobs,
					  'jobs_list':jobs_list,
					  'total_featured_jobs':total_featured_jobs,
					  'category_list':category_list})

	else:

		search = request.POST['search']

		all_jobs = len(job.get_jobs_list())
		jobs_result_list = job.get_jobs_result_list(search)
		category_list = categories.get_category_list()

		return render(request, 'jobs/job_result.html',
					 {'all_jobs':all_jobs,
					  'jobs_list':jobs_result_list,
					  'category_list':category_list})


def jobs_result(request, tag):

	all_jobs = len(job.get_jobs_list())
	jobs_result_list = job.get_jobs_result_by_tag(tag)
	category_list = categories.get_category_list()

	return render(request, 'jobs/job_result.html',
					 {'all_jobs':all_jobs,
					  'jobs_list':jobs_result_list,
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
		salary = request.POST['salary']
		tags = request.POST['tags']
		headquarters = request.POST['headquarters']
		region = request.POST['region']
		link = request.POST['link']
		job_description = request.POST['job_description']

		if 'featured' in request.POST:
			is_featured = request.POST['featured']
		else:
			is_featured = False
		
		name = request.POST['company_name']
		logo = request.FILES['logo']
		tagline = request.POST['tagline']
		initial_website = request.POST['website']

		if initial_website[:4] == "www.":
			final_website = initial_website[4:]
		else:
			final_website = initial_website

		email = request.POST['email']
		company_description = request.POST['company_description']

		company_exist = company.check_company_exist(final_website)


		if company_exist:

			jobSlugTitle = job.create_new_job(final_website, title, category, job_type, salary, tags, headquarters, region, link, job_description, is_featured)

			companyName = company.get_company_by_website(final_website)

			context_data = {'jobSlugTitle':jobSlugTitle, 'jobName':title, 'companyName':companyName}

			return render(request, 'jobs/job_success.html', context=context_data)

		else:

			jobSlugTitle = job.create_new_job(final_website, title, category, job_type, salary, tags, headquarters, region, link, job_description, is_featured)

			company.create_new_company(name, logo, tagline, final_website, email, company_description)

			companyName = company.get_company_by_website(final_website)

			context_data = {'jobSlugTitle':jobSlugTitle, 'jobName':title, 'companyName':companyName}

			return render(request, 'jobs/job_success.html', context=context_data)


def job_detail(request, jobName):

	job_detail = job.get_job_name(jobName)
	category_name = job.get_category_name(jobName)
	all_jobs = len(job.get_jobs_list())
	category_list = categories.get_category_list()
	company_detail = company.get_company_by_job_name(jobName)
	job_posted_by_company = len(company.get_company_job_posted(jobName))

	related_jobs = job.get_related_jobs(jobName)

	return render(request, 'jobs/job_detail.html',
				 {'job':job_detail,
				  'all_jobs':all_jobs,
				  'job_posted':job_posted_by_company,
				  'related_jobs':related_jobs,
				  'company':company_detail,
				  'category_name':category_name,
				  'category_list':category_list})


def billing(request):

	all_jobs = len(job.get_jobs_list())
	category_list = categories.get_category_list()

	return render(request, 'jobs/billing.html',
				 {'all_jobs':all_jobs,
				  'category_list':category_list})


def jobfeed(request, post_id=id):

	item = get_object_or_404(Post, id=post_id)

	return render(request, {'job-feed': item})
	
	
def post(request, post_id=id):

	item = get_object_or_404(Post, id=post_id)

	return render(request, {'post': item})


def success(request):

	all_jobs = len(job.get_jobs_list())
	category_list = categories.get_category_list()

	return render(request, 'jobs/job_success.html',
				 {'all_jobs':all_jobs,
				  'category_list':category_list})


