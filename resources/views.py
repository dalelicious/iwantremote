# Django
from django.http 			import HttpResponse
from django.shortcuts 		import render
from django.shortcuts 		import redirect


def blog(request):

	return render(request, 'resources/blog.html')