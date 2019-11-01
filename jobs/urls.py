from django.urls import path
from jobs.feed import LatestEntriesFeed

from . import views

app_name = 'jobs'

urlpatterns = [
    path('jobs/', 						views.jobs, 		name='jobs'),
    path('create_job/', 				views.create_job, 	name='create-job'),
    path('remote-jobs/<slug:jobName>/', 	views.job_detail, 	name='job-detail'),
    path('billing/', 	views.billing, 	name='billing'),
    path('feed/', LatestEntriesFeed())
]