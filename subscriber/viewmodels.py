# Django
from django.utils 	import timezone

# Subscriber
from . models 		import Subscriber


class SubscriberViewModel():


	def add_new_subscriber(self, email):
		""" Add new feedback
		"""

		subscriber = Subscriber()
		subscriber.email = email

		self.save_to_subscriber(subscriber)


	def save_to_subscriber(self, subscriber):
		""" Save subscriber to database
		"""

		subscriber.save()
