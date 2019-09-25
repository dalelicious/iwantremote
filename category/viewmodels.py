# Category
from . models 		import Category


class CategoryViewModel():


	def get_category_list(self):
		""" Get all category
		"""

		category_list = Category.objects.all()

		return category_list


	def get_category_by_id(self, categoryId):
		""" Get all category by id
		"""

		category = Category.objects.get(id=categoryId)

		return category