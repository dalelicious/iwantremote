# Django
from django.http 			import HttpResponse
from django.shortcuts 		import render
from django.shortcuts 		import redirect

from . viewmodels 			import SubscriberViewModel


subscribers = SubscriberViewModel()

def confirmation(request):

	return render(request, 'subscriber/confirmation.html')

def add_subscriber(request):

	email = request.POST['email']

	subscribers.add_new_subscriber(email)

	return redirect('subscriber:sub_confirmation')

