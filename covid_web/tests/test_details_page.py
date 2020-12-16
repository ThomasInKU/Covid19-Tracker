"""Unittests for Django polls application."""
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils.http import urlencode
from covid_web.covid_data import CountryCovidData, ThailandCovidData
from covid_web.views import get_location_form_ip


def my_reverse(viewname, kwargs=None, query_kwargs=None):
    """Add a query string after the url.

    Example usage:
    url = my_reverse('my_test_url',
    kwargs={'pk': object.id}, query_kwargs={'next': reverse('home')})
    """
    url = reverse(viewname, kwargs=kwargs)

    if query_kwargs:
        return u'%s?%s' % (url, urlencode(query_kwargs))

    return url


class IndexPageTest(TestCase):
    """Index page test."""

    def setUp(self):
        """Set up method for everything that use in test."""
        User.objects.create_user(username='bhatara007', password='ddddd007')
        self.client.login(username='bhatara007', password='ddddd007')

    def test_details_page_display_correctly(self):
        """
         Test Covid data show correctly.

        When user selected Thailand country.
        """
        test_country = 'Thailand'
        cd = CountryCovidData()
        url = my_reverse('details',
                         kwargs=None, query_kwargs={'country': test_country})
        response = self.client.get(url)
        self.assertContains(response, "{:,}".
                            format(cd.get_result("cases", "Thailand")))
        self.assertContains(response, "{:,}".
                            format(cd.get_result("todayCases", "Thailand")))
        self.assertContains(response, "{:,}".
                            format(cd.get_result("deaths", "Thailand")))
        self.assertContains(response, "{:,}".
                            format(cd.get_result("todayDeaths", "Thailand")))

    def test_user_location_form_ip(self):
        """Test for get_user_country_form_ip method if we put our ip.

        This method will return our current country "Thailand".
        """
        my_current_ip = '49.229.136.171'
        my_current_country = "Thailand"
        self.assertEqual(my_current_country,
                         get_location_form_ip(my_current_ip)["country_name"])

    def test_prevent_page(self):
        """Test can access prevent page."""
        url = reverse('prevent')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_map_can_access(self):
        """Test can access map page."""
        url = reverse('map')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_details_show_in_map_correctly(self):
        """Test map show in details page."""
        test_province = "Nan"
        url = my_reverse('map', kwargs=None,
                         query_kwargs={'province': test_province})
        td = ThailandCovidData()
        data = "{:,}".format(td.get_result(test_province))
        response = self.client.get(url)
        self.assertContains(response, data)
