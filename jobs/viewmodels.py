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


	def create_new_job(self, job_title, category, job_type, headquarters, region, apply_link, job_description):
		""" Create new job
		"""

		job = Jobs()
		job.job_title = job_title
		job.category = category
		job.job_type = job_type
		job.headquarters = headquarters
		job.region = region
		job.apply_link = apply_link
		job.job_description = job_description

		self.save_to_jobs(job)		


	def save_to_jobs(self, job):
		""" Save job to database
		"""

		job.save()