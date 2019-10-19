# Django
from django.http 			import HttpResponse
from django.shortcuts 		import render
from django.shortcuts 		import redirect

from . viewmodels 			import FeedbackViewModel
from jobs.viewmodels 		import JobsViewModel

job = JobsViewModel()


feedbacks = FeedbackViewModel()


def feedback(request):

	all_jobs = len(job.get_jobs_list())

	return render(request, 'feedback/feedback.html',
				 {'all_jobs':all_jobs})
	

def confirmation(request):

	all_jobs = len(job.get_jobs_list())

	return render(request, 'feedback/confirmation.html',
				 {'all_jobs':all_jobs})


def create_feedback(request):

	name = request.POST['name']
	job_title = request.POST['job_title']
	content = request.POST['feedback_content']

	feedbacks.create_new_feedback(name, job_title, content)

	return redirect('feedback:confirmation')