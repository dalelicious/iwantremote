# Django
from django.http 			import HttpResponse
from django.shortcuts 		import render
from django.shortcuts 		import redirect

# iwantremote
from . viewmodels 			import CategoryViewModel
from jobs.viewmodels 		import JobsViewModel


job = JobsViewModel()
category = CategoryViewModel()


def categories(request, categoryName):

	all_jobs = len(job.get_jobs_list())
	categories = category.get_category_by_name(categoryName)
	jobs_list = job.get_jobs_list_by_category(categoryName)
	category_list = category.get_category_list()


	return render(request, 'category/category.html',
				 {'all_jobs':all_jobs,
				  'jobs_list':jobs_list,
				  'categories':categories,
				  'category_list':category_list})