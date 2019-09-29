# Django
from django.http 			import HttpResponse
from django.shortcuts 		import render
from django.shortcuts 		import redirect

from . viewmodels 			import ResourcesViewModel


resources = ResourcesViewModel()


def blog(request):

	blog_list = resources.get_blog_list()

	return render(request, 'resources/blog.html',
				 {'blog_list':blog_list})


def blog_detail(request, blogId):

	blog = resources.get_blog_by_id(blogId)

	return render(request, 'resources/blog_detail.html',
				 {'blog':blog})


def privacy(request):

	return render(request, 'resources/privacy.html')