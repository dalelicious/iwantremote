# Django
from django.utils 	import timezone

# Feedback
from . models 		import Feedback


class FeedbackViewModel():


	def create_new_feedback(self, name, content):
		""" Create new feedback
		"""

		feedback = Feedback()
		feedback.name = name
		feedback.content = content
		feedback.create_date = timezone.now()

		self.save_to_feedback(feedback)


	def save_to_feedback(self, feedback):
		""" Save feedback to database
		"""

		feedback.save()
