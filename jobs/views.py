# Django
from django.http 			import HttpResponse
from django.shortcuts 		import render
from django.shortcuts 		import redirect

# iwantremote
from . viewmodels 			import JobsViewModel
from company.viewmodels 	import CompanyViewModel


job = JobsViewModel()
company = CompanyViewModel()


def jobs(request):

	jobs_list = job.get_jobs_list()

	return render(request, 'jobs/jobs.html',
				 {'jobs_list' : jobs_list})


def create_job(request):

	if request.method == "GET":

		return render(request, 'jobs/create_jobs.html')

	else:

		title = request.POST['title']
		category = request.POST['category']
		job_type = request.POST['job_type']
		headquarters = request.POST['headquarters']
		region = request.POST['region']
		link = request.POST['link']
		job_description = request.POST['job_description']

		name = request.POST['company_name']
		logo = request.POST['logo']
		tagline = request.POST['tagline']
		website = request.POST['website']
		email = request.POST['email']
		company_description = request.POST['company_description']

		job.create_new_job(email, title, category, job_type, headquarters, region, link, job_description)

		company.create_new_company(name, logo, tagline, website, email, company_description)

		return redirect('jobs:jobs')


def job_detail(request, jobId):

	job_detail = job.get_job_id(jobId)
	company_detail = company.get_company_by_job_id(jobId)

	return render(request, 'jobs/job_detail.html',
				 {'job' : job_detail,
				  'company' : company_detail})


