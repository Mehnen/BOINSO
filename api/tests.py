from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import (
    APITestCase, APIClient, APIRequestFactory, force_authenticate)

from oauth2_provider.models import Application

from api.views import UserProfileProxy


class ApiRootTests(APITestCase):

    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            'admin', 'admin@admin.at', 'adminpw')
        self.normal_user = User.objects.create_user(
            'bobben', 'bobben@bob.at', 'bobbenpw')
        self.client = APIClient()

    def test_call_api_root(self):
        """
        Ensure API Root is allways callable and returns links.
        """
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserProfileTests(APITestCase):

    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            'admin', 'admin@admin.at', 'adminpw')
        self.normal_user = User.objects.create_user(
            'bobben', 'bobben@bob.at', 'bobbenpw')
        self.client = APIClient()
        self.req_factory = APIRequestFactory()
        # self.admin_application = Application(
        #     user=self.admin_user,
        #     client_type=Application.CLIENT_CONFIDENTIAL,
        #     authorization_grant_type=Application.GRANT_PASSWORD
        # )
        # self.admin_application.save()

    def test_call_user_profile_proxy_without_auth(self):
        """
        Ensure unauthenticated user gets 4001
        """
        response = self.client.get('/api/user-profiles/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_call_user_profile_proxy_with_auth(self):
    #     view = UserProfileProxy.as_view()
    #     request = self.req_factory.get('/api/user-profiles/')
    #     force_authenticate(request, user=self.admin_user)
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
