"""Unittests for Django polls application."""
import datetime
import unittest

from covid_web.covid_data import CountryCovidData, WorldCovidData
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse


class IndexPageTest(TestCase):

    def test_world_detail_display_correctly(self):
        cd = WorldCovidData()
        url = reverse('index')
        response = self.client.get(url)
        cases = "{:,}".format(cd.get_result("cases"))
        today_case = "{:,}".format(cd.get_result("todayCases"))
        deaths = "{:,}".format(cd.get_result("deaths"))
        new_deaths = "{:,}".format(cd.get_result("todayDeaths"))
        self.assertContains(response, cases)
        self.assertContains(response, today_case)
        self.assertContains(response, deaths)
        self.assertContains(response, new_deaths)
        









