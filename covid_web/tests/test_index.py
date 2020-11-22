"""Unittests for Django polls application."""
from covid_web.covid_data import WorldCovidData
from django.test import TestCase
from django.urls import reverse


class IndexPageTest(TestCase):

    def test_world_detail_display_correctly(self):
        """test the covid data displays on details page correctly"""
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
    
    def test_can_access_sign_up_page(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
