# Django
from django.http 			import HttpResponse
from django.shortcuts 		import render
from django.shortcuts 		import redirect

from . viewmodels 			import ResourcesViewModel
from jobs.viewmodels 	import JobsViewModel
from category.viewmodels 	import CategoryViewModel


job = JobsViewModel()
resources = ResourcesViewModel()
categories = CategoryViewModel()


def blog(request):

	all_jobs = len(job.get_jobs_list())
	blog_list = resources.get_blog_list()
	category_list = categories.get_category_list()

	return render(request, 'resources/blog.html',
				 {'all_jobs':all_jobs,
				  'blog_list':blog_list,
				  'category_list':category_list})


def blog_detail(request, blogId):

	all_jobs = len(job.get_jobs_list())
	blog = resources.get_blog_by_id(blogId)
	category_list = categories.get_category_list()

	return render(request, 'resources/blog_detail.html',
				 {'all_jobs':all_jobs,
				  'blog':blog,
				  'category_list':category_list})


def privacy(request):

	all_jobs = len(job.get_jobs_list())
	category_list = categories.get_category_list()

	return render(request, 'resources/privacy.html',
				 {'all_jobs':all_jobs,
				  'category_list':category_list})

def job_template(request):

	all_jobs = len(job.get_jobs_list())
	category_list = categories.get_category_list()

	return render(request, 'resources/job_template.html',
				 {'all_jobs':all_jobs,
				  'category_list':category_list})