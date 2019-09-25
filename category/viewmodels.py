# Category
from . models 		import Category


class CategoryViewModel():


	def get_category_list(self):
		""" Get all category
		"""

		category_list = Category.objects.all()

		return category_list