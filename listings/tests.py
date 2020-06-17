from django.test import TestCase,Client
from django.urls import reverse
# from .models import Listing

# Create your tests here.

class TestModel(TestCase):
	
	def test_listing(self):
		client = Client()
		response = client.get(reverse('listings'))


		self.assertTemplateUsed(response,'listings/listings.htmls')
