# Django
from django 						import forms
from django.db 						import models
from django.contrib 				import admin

# iwantremote
from resources.models 				import Resources


class ResourcesAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'author', 'content', 'create_date', 'blog_image')

	def formfield_for_dbfield(self, db_field, **kwargs):
		formfield = super(ResourcesAdmin, self).formfield_for_dbfield(db_field, **kwargs)
		if db_field.name == 'content':
			formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
		return formfield


admin.site.register(Resources, ResourcesAdmin)