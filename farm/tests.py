# from rest_framework.test import requests
import requests
from rest_framework.test import APITestCase
from rest_framework import status


class DivisionTestCase(APITestCase):

    def test_division(self):

        response = requests.get('http://localhost:8000/api/division/')
        # print(f"response: {response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_district(self):

        response = requests.get('http://localhost:8000/api/district/')
        # print(f"response: {response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_upazila(self):

        response = requests.get('http://localhost:8000/api/upazila/')
        # print(f"response: {response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)