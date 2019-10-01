# Company
from . models import Company
from jobs.models import Jobs


class CompanyViewModel():


	def get_company_by_id(self, companyId):
		""" Get company id
		"""

		company = Company.objects.get(id=companyId)

		return company


	def get_company_by_job_id(self, jobId):
		""" Get company by job id
		"""

		job = Jobs.objects.get(id=jobId)
		company = Company.objects.get(email=job.company)

		return company


	def get_company_list(self):
		""" Get all company
		"""

		company_list = Company.objects.all()

		return company_list


	def get_all_job_posted(self, companyId):
		""" Get all job posted
		"""

		company = Company.objects.get(id=companyId)
		job_posted = Jobs.objects.filter(company=company.email)

		return job_posted


	def create_new_company(self, name, logo, tagline, website, email, company_description):
		""" Create new company
		"""

		company = Company()
		company.name = name
		company.logo = logo
		company.tagline = tagline
		company.website = website
		company.email = email
		company.description = company_description

		self.save_to_company(company)


	def company_exist(self, email):
		""" Check if company already exist
		"""

		company = Company.objects.get(email=email)

		if company:
			return True
		else:
			return False


	def save_to_company(self, company):
		""" Save company to database
		"""

		company.save()