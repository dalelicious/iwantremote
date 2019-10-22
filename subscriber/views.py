# Django
from django.http 			import HttpResponse
from django.shortcuts 		import render
from django.shortcuts 		import redirect

from . viewmodels 			import SubscriberViewModel
from category.viewmodels 	import CategoryViewModel


subscribers = SubscriberViewModel()
categories = CategoryViewModel()


def confirmation(request):

	category_list = categories.get_category_list()

	return render(request, 'subscriber/confirmation.html',
				 {'category_list':category_list})

def add_subscriber(request):

	email = request.POST['email']
	category = request.POST['category']

	subscribers.add_new_subscriber(email, category)

	return redirect('subscriber:sub_confirmation')

