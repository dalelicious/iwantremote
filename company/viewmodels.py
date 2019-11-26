import re
import string
import random

# Company
from . models import Company
from jobs.models import Jobs


class CompanyViewModel():


	def get_company_by_name(self, companyName):
		""" Get company name
		"""

		company = Company.objects.get(slugName=companyName)

		return company

	def get_company_by_website(self, companyWebsite):
		""" Get company by website
		"""

		company = Company.objects.get(website=companyWebsite)

		return company.name


	def get_company_by_job_name(self, jobName):
		""" Get company by job name
		"""

		job = Jobs.objects.get(slugTitle=jobName)
		company = Company.objects.get(website=job.company)

		return company


	def get_company_list(self):
		""" Get all company sorted by job posted
		"""

		company_list = sorted(Company.objects.all(), key=lambda t: t.total_job_posted, reverse=True)

		return company_list


	def get_all_job_posted(self, companyName):
		""" Get all job posted
		"""

		company = Company.objects.get(slugName=companyName)
		job_posted = Jobs.objects.filter(company=company.website)

		return job_posted


	def get_company_job_posted(self, jobName):
		""" Get company job posted
		"""

		job = Jobs.objects.get(slugTitle=jobName)
		company = Company.objects.get(website=job.company)
		job_posted = Jobs.objects.filter(company=company.website)

		return job_posted


	def get_company_headquarters(self, companyName):
		""" Get company headquarters
		"""

		headquarters_list = []

		company = Company.objects.get(slugName=companyName)
		jobs = Jobs.objects.filter(company=company.website)

		for job in jobs:
			headquarters_list.append(job.headquarters)

		return max(set(headquarters_list), key=headquarters_list.count)


	def check_company_exist(self, website):
		""" Check if email exist
		"""

		company = Company.objects.filter(website=website)

		if len(company) > 0:
			return True
		else:
			return False


	def remove_special_chars(self, name):
		""" Remove special characters from string
		"""

		for k in name.split("\n"):
			compName = re.sub(r"[^a-zA-Z0-9]+", ' ', k)


		return compName


	def create_new_company(self, name, logo, tagline, website, email, company_description):
		""" Create new company
		"""

		name_pattern = string.digits
		combi = "".join(random.choice(name_pattern) for x in range(4))

		specialCompName = name + " " + combi

		compName = self.remove_special_chars(specialCompName)

		company = Company()
		company.name = specialCompName
		company.slugName = compName.replace(" ", "-").lower()
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