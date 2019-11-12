from django.urls import path
from jobs.feed import LatestEntriesFeed

from . import views

app_name = 'jobs'

urlpatterns = [
    path('', 								views.jobs, 		name='jobs'),
    path('billing/', 						views.billing, 		name='billing'),
    path('success/', 						views.success, 		name='success'),
    path('create_job/', 					views.create_job, 	name='create-job'),
    path('jobs_result/<slug:tag>/',			views.jobs_result,	name='jobs-result'),
    path('remote-jobs/<slug:jobName>/', 	views.job_detail, 	name='job-detail'),
    path('feed/', LatestEntriesFeed())
]