"""Unittests for Django polls application."""
import datetime
import unittest

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

class UserAuthenticationTest(TestCase):
    
        def test_user_login_success(self):
            User.objects.create_user(username='bhatara007', password='ddddd007')
            self.client.login(username='bhatara007', password='ddddd007')
            url = reverse('details')
            response = self.client.get(url)
            self.assertContains(response, "bhatara007")
        
        def test_authenticated_user_can_access_details_page(self):
            User.objects.create_user(username='bhatara007', password='ddddd007')
            self.client.login(username='bhatara007', password='ddddd007')
            url = reverse('details')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
        
        def test_user_not_login(self):
            self.client.login(username='bhatara007', password='ddddd007')
            url = reverse('details')
            response = self.client.get(url)
            login_url = '/accounts/login/?next=/country/'
            self.assertRedirects(response, login_url)


            
        
        
        
        

            
                