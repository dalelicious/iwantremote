# Django
from django.http 			import HttpResponse
from django.shortcuts 		import render
from django.shortcuts 		import redirect

# iwantremote
from . viewmodels 			import CategoryViewModel


category = CategoryViewModel()


def categories(request):

	category_list = category.get_category_list()

	return render(request, 'templates/header.html',
				 {'category_list':category_list})