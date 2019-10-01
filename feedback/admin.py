# Django
from django.db 						import models
from django.contrib 				import admin

# iwantremote
from feedback.models 				import Feedback


class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'content', 'create_date')


admin.site.register(Feedback, FeedbackAdmin)