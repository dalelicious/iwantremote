# Django
from django.db 						import models
from django.contrib 				import admin

# iwantremote
from company.models 				import Company


class CompanyAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'email', 'logo', 'tagline', 'website', 'description')


admin.site.register(Company, CompanyAdmin)