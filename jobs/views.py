# Django
from django.http 		import HttpResponse
from django.shortcuts 	import render
from django.shortcuts 	import redirect

# Wifi Users
from . viewmodels 		import JobsViewModel


job = JobsViewModel()


def jobs(request):

	jobs_list = job.get_jobs_list()

	return render(request, 'jobs/jobs.html',
				 {'jobs_list' : jobs_list})


def create_job(request):

	if request.method == "GET":

		return render(request, 'jobs/create_jobs.html')

	else:

		job_title = request.POST['job_title']
		category = request.POST['category']
		job_type = request.POST['job_type']
		headquarters = request.POST['headquarters']
		region = request.POST['region']
		apply_link = request.POST['apply_link']
		job_description = request.POST['job_description']

		job.create_new_job(job_title, category, job_type, headquarters, region, apply_link, job_description)

		return redirect('jobs:jobs')
