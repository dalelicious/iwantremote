# Django
from django.db 						import models
from django.contrib 				import admin

# iwantremote
from resources.models 				import Resources


class ResourcesAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'author', 'content', 'create_date', 'blog_image')


admin.site.register(Resources, ResourcesAdmin)