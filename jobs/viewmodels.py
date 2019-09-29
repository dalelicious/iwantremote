# Django
from django.utils 	import timezone

# Jobs
from . models 		import Jobs


class JobsViewModel():


	def get_job_id(self, jobId):
		""" Get job id
		"""

		job = Jobs.objects.get(id=jobId)

		return job


	def get_jobs_list(self):
		""" Get all jobs
		"""

		jobs_list = Jobs.objects.all()

		return jobs_list


	def get_job_results(self, search):
		""" Get job search results
		"""

		jobs_list = Jobs.objects.filter(title__icontains=search)

		return jobs_list


	def get_featured_jobs_list(self):
		""" Get all featured jobs
		"""

		jobs_list = Jobs.objects.filter(is_featured=True)

		return jobs_list


	def get_jobs_list_by_category(self, categoryId):
		""" Get all jobs by category
		"""

		jobs_list = Jobs.objects.filter(category=categoryId)

		return jobs_list


	def create_new_job(self, email, title, category, job_type, headquarters, region, link, job_description, is_featured):
		""" Create new job
		"""

		job = Jobs()
		job.company = email
		job.title = title
		job.category = category
		job.job_type = job_type
		job.headquarters = headquarters
		job.region = region
		job.link = link
		job.description = job_description
		job.create_date = timezone.now()
		job.is_active = True
		job.is_featured = is_featured

		self.save_to_jobs(job)


	def save_to_jobs(self, job):
		""" Save job to database
		"""

		job.save()


		