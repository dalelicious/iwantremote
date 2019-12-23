# Django
from django.utils 	import timezone

# Resources
from . models 		import Resources


class ResourcesViewModel():


	def get_blog_by_name(self, blogTitle):
		""" Get blog by id
		"""

		blog = Resources.objects.get(slugTitle=blogTitle)

		return blog


	def get_blog_list(self):
		""" Get all blog
		"""

		blog_list = Resources.objects.all()

		return blog_list

