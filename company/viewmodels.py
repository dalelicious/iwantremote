# Company
from . models import Company
from jobs.models import Jobs


class CompanyViewModel():


	def get_company_by_name(self, companyName):
		""" Get company name
		"""

		company = Company.objects.get(slugName=companyName)

		return company


	def get_company_by_job_name(self, jobName):
		""" Get company by job name
		"""

		job = Jobs.objects.get(slugTitle=jobName)
		company = Company.objects.get(email=job.company)

		return company


	def get_company_list(self):
		""" Get all company
		"""

		company_list = Company.objects.all()

		return company_list


	def get_all_job_posted(self, companyName):
		""" Get all job posted
		"""

		company = Company.objects.get(slugName=companyName)
		job_posted = Jobs.objects.filter(company=company.email)

		return job_posted


	def check_company_exist(self, email):
		""" Check if email exist
		"""

		company = Company.objects.filter(email=email)

		if len(company) > 0:
			return True
		else:
			return False


	def create_new_company(self, name, logo, tagline, website, email, company_description):
		""" Create new company
		"""

		company = Company()
		company.name = name
		company.slugName = name.replace(" ", "-").lower()
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