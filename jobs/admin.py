# Django
from django.db 						import models
from django.contrib 				import admin

# iwantremote
from jobs.models 					import Jobs


class JobsAdmin(admin.ModelAdmin):
	list_display = ('id', 'company', 'title', 'category', 'job_type', 'headquarters', 'region', 'link', 'description', 'create_date')


admin.site.register(Jobs, JobsAdmin)