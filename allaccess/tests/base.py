"Base test class and helper methods for writing tests."
from __future__ import unicode_literals

import random
import string

from django.contrib.auth.models import User
from django.test import TestCase

from allaccess.models import Provider, AccountAccess


class AllAccessTestCase(TestCase):
    "Common base test class."

    def get_random_string(self, length=10):
        "Create a random string for generating test data."
        return ''.join(random.choice(string.ascii_letters) for x in xrange(length))

    def get_random_email(self, domain='example.com'):
        "Create a random email for generating test data."
        local = self.get_random_string()
        return '{0}@{1}'.format(local, domain)
    
    def get_random_url(self, domain='example.com'):
        "Create a random url for generating test data."
        path = self.get_random_string()
        return 'http://{0}/{1}'.format(domain, path)

    def create_user(self, **kwargs):
        "Create a test User"
        defaults = {
            'username': self.get_random_string(),
            'password': self.get_random_string(),
            'email': self.get_random_email()
        }
        defaults.update(kwargs)
        return User.objects.create_user(**defaults)

    def create_provider(self, **kwargs):
        "Create OAuth provider."
        defaults = {
            'name': self.get_random_string(),
            'authorization_url': self.get_random_url(),
            'access_token_url': self.get_random_url(),
            'profile_url': self.get_random_url(),
        }
        defaults.update(kwargs)
        return Provider.objects.create(**defaults)

    def create_access(self, **kwargs):
        "Create a test remote AccountAccess"
        defaults = {
            'identifier': self.get_random_string(),
        }
        defaults.update(kwargs)
        if 'provider' not in defaults:
            defaults['provider'] =  self.create_provider()
        return AccountAccess.objects.create(**defaults)
