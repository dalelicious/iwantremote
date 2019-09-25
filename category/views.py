# Django
from django.http 			import HttpResponse
from django.shortcuts 		import render
from django.shortcuts 		import redirect

# iwantremote
from . viewmodels 			import CategoryViewModel
from jobs.viewmodels 		import JobsViewModel


job = JobsViewModel()
category = CategoryViewModel()


def categories(request, categoryId):

	categories = category.get_category_by_id(categoryId)
	jobs_list = job.get_jobs_list_by_category(categoryId)
	category_list = category.get_category_list()


	return render(request, 'category/category.html',
				 {'jobs_list':jobs_list,
				  'category_list':category_list})