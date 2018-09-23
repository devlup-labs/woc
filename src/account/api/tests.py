from django.test import TestCase
from django.shortcuts import reverse
from rest_framework import status
from account.models import StudentProfile
from account.models import MentorProfile
from django.contrib.auth.models import User


class StudentProfileViewSetTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='student', password='password')

    def test_bad_request(self):
        response = self.client.post(reverse('api:account:student-profile-list'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_created(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': StudentProfile.GENDER_CHOICES[0][0],
            'branch': StudentProfile.BRANCH_CHOICES[0][0],
            'year': StudentProfile.YEAR_CHOICES[0][0],
            'user': self.user.id
        }
        response = self.client.post(reverse('api:account:student-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_missing_user_id(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': StudentProfile.GENDER_CHOICES[0][0],
            'branch': StudentProfile.BRANCH_CHOICES[0][0],
            'year': StudentProfile.YEAR_CHOICES[0][0],
        }
        response = self.client.post(reverse('api:account:student-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content.decode('utf-8'), '{"user":["This field is required."]}')

    def test_invalid_user_id(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': StudentProfile.GENDER_CHOICES[0][0],
            'branch': StudentProfile.BRANCH_CHOICES[0][0],
            'year': StudentProfile.YEAR_CHOICES[0][0],
            'user': self.user.id + 12
        }
        response = self.client.post(reverse('api:account:student-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content.decode('utf-8'), '{"user":["Invalid pk \\"13\\" - object does not exist."]}')


class MentorProfileViewSetTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='mentor', password='password')

    def test_bad_request(self):
        response = self.client.post(reverse('api:account:mentor-profile-list'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_created(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': MentorProfile.GENDER_CHOICES[0][0],
            'user': self.user.id
        }
        response = self.client.post(reverse('api:account:mentor-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_missing_user_id(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': MentorProfile.GENDER_CHOICES[0][0],
        }
        response = self.client.post(reverse('api:account:mentor-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content.decode('utf-8'), '{"user":["This field is required."]}')

    def test_invalid_user_id(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': MentorProfile.GENDER_CHOICES[0][0],
            'user': self.user.id + 12
        }
        response = self.client.post(reverse('api:account:mentor-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content.decode('utf-8'), '{"user":["Invalid pk \\"13\\" - object does not exist."]}')
