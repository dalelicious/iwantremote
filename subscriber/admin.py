# Django
from django.db 						import models
from django.contrib 				import admin

# iwantremote
from subscriber.models 				import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
	list_display = ('id', 'email')


admin.site.register(Subscriber, SubscriberAdmin)