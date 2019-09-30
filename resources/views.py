# Django
from django.http 			import HttpResponse
from django.shortcuts 		import render
from django.shortcuts 		import redirect

from . viewmodels 			import ResourcesViewModel
from category.viewmodels 	import CategoryViewModel


resources = ResourcesViewModel()
categories = CategoryViewModel()


def blog(request):

	blog_list = resources.get_blog_list()
	category_list = categories.get_category_list()

	return render(request, 'resources/blog.html',
				 {'blog_list':blog_list,
				  'category_list':category_list})


def blog_detail(request, blogId):

	blog = resources.get_blog_by_id(blogId)
	category_list = categories.get_category_list()

	return render(request, 'resources/blog_detail.html',
				 {'blog':blog,
				  'category_list':category_list})


def privacy(request):

	return render(request, 'resources/privacy.html')