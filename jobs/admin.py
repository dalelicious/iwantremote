# Django
from django.db 						import models
from django.contrib 				import admin

# iwantremote
from jobs.models 					import Jobs


class JobsAdmin(admin.ModelAdmin):
	list_display = ('id', 'company', 'title', 'slugTitle', 'category', 'job_type', 'salary', 'tags', 'headquarters', 'region', 'link', 'description', 'create_date')


admin.site.register(Jobs, JobsAdmin)