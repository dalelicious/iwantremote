# Jobs
from . models import Jobs


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


	def create_new_job(self, email, title, category, job_type, headquarters, region, link, job_description):
		""" Create new job
		"""

		job = Jobs()
		job.company = email
		job.title = title
		job.category = category
		job.job_type = job_type
		job.headquarters = headquarters
		job.region = region
		job.apply_link = link
		job.description = job_description

		self.save_to_jobs(job)		


	def save_to_jobs(self, job):
		""" Save job to database
		"""

		job.save()