"""Unittests for Django polls application."""
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class IndexPageTest(TestCase):
    def setUp(self):
        """set up method for set everythings that use in test"""
        User.objects.create_user(username='bhatara007', password='ddddd007')
        self.client.login(username='bhatara007', password='ddddd007')

    def test_blank_detail_page(self):
        """
        test 'Let's find your Interesting area' text show
        when user not select thier area
        """
        url = reverse('details')
        response = self.client.get(url)
        self.assertContains(response, "Let's find your Interested area")
