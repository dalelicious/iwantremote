# Django
from django.db 						import models
from django.contrib 				import admin

# iwantremote
from category.models 				import Category


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')


admin.site.register(Category, CategoryAdmin)