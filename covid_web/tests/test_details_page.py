"""Unittests for Django polls application."""
import datetime
import unittest

from covid_web.covid_data import CountryCovidData, WorldCovidData
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse


class IndexPageTest(TestCase):
    
    def setUp(self):
        User.objects.create_user(username='bhatara007', password='ddddd007')
        self.client.login(username='bhatara007', password='ddddd007')

    def test_blank_detail_page(self):
        url = reverse('details')
        response = self.client.get(url)
        self.assertContains(response, 'please select the country')
    
    # def test_detail_page(self):
    #     url = reverse('details/$', args= ["Thailand"])
    #     response = self.client.get(url)
    #     self.assertNotContains(response, 'please select the country')
        