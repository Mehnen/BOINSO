from django.test import TestCase
from django.contrib.auth.models import User
from core.models import UserProfile


class UserProfileTests(TestCase):

    """
    Test cases covering the basic functionality of the
    UserProfile Model
    """

    def setUp(self):
        self.test_user = User(username="testi")
        self.test_user.set_password('testi')
        self.test_user.save()

    def test_that_model_can_be_created_from_userside(self):
        self.test_user.userprofile = UserProfile(latitude=12.45)
        self.assertEqual(self.test_user.userprofile.latitude, 12.45)
