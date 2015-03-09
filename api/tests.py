from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
# from .views import api_root, UserList, UserDetail


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
