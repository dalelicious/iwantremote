# Django
from django.http 			import HttpResponse
from django.shortcuts 		import render
from django.shortcuts 		import redirect

from . viewmodels 			import FeedbackViewModel


feedbacks = FeedbackViewModel()


def feedback(request):

	return render(request, 'feedback/feedback.html')


def create_feedback(request):

	name = request.POST['name']
	job_title = request.POST['job_title']
	content = request.POST['feedback_content']

	feedbacks.create_new_feedback(name, job_title, content)

	return redirect('jobs:jobs')