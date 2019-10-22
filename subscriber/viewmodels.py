# Django
from django.utils 	import timezone

# Subscriber
from . models 		import Subscriber


class SubscriberViewModel():


	def add_new_subscriber(self, email, category):
		""" Add new feedback
		"""

		subscriber = Subscriber()
		subscriber.email = email
		subscriber.category = category

		self.save_to_subscriber(subscriber)


	def save_to_subscriber(self, subscriber):
		""" Save subscriber to database
		"""

		subscriber.save()
