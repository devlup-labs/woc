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
        self.client.login(username=self.user.username, password='password')
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
        self.client.login(username=self.user.username, password='password')
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
        self.client.login(username=self.user.username, password='password')
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
        self.client.login(username=self.user.username, password='password')
        response = self.client.post(reverse('api:account:student-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content.decode('utf-8'), '{"user":["Invalid pk \\"13\\" - object does not exist."]}')


class MentorProfileViewSetTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='mentor', password='password')

    def test_bad_request(self):
        self.client.login(username=self.user.username, password='password')
        response = self.client.post(reverse('api:account:mentor-profile-list'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_created(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': MentorProfile.GENDER_CHOICES[0][0],
            'user': self.user.id,
            'past_experience': 'None',
            'about_me': 'Expert'
        }
        self.client.login(username=self.user.username, password='password')
        response = self.client.post(reverse('api:account:mentor-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_missing_user_id(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': MentorProfile.GENDER_CHOICES[0][0],
            'past_experience': 'None',
            'about_me': 'Expert'
        }
        self.client.login(username=self.user.username, password='password')
        response = self.client.post(reverse('api:account:mentor-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content.decode('utf-8'), '{"user":["This field is required."]}')

    def test_invalid_user_id(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': MentorProfile.GENDER_CHOICES[0][0],
            'user': self.user.id + 12,
            'past_experience': 'None',
            'about_me': 'Expert'
        }
        self.client.login(username=self.user.username, password='password')
        response = self.client.post(reverse('api:account:mentor-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content.decode('utf-8'), '{"user":["Invalid pk \\"13\\" - object does not exist."]}')


class UserViewSetTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='mentor', password='password')

    def test_get_current_user(self):
        response = self.client.get(reverse('api:account:user-current'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.login(username=self.user.username, password='password')
        response = self.client.get(reverse('api:account:user-current'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_with_no_profile_type(self):
        self.client.login(username=self.user.username, password='password')
        response = self.client.get(reverse('api:account:user-profile'))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_with_mentor_profile(self):
        self.client.login(username=self.user.username, password='password')
        self.mentor_profile = MentorProfile.objects.create(user=self.user)
        response = self.client.get(reverse('api:account:user-profile'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '{"type":"mentor-profile","id":%s}' % self.mentor_profile.id)

    def test_user_with_student_profile(self):
        self.client.login(username=self.user.username, password='password')
        self.student_profile = StudentProfile.objects.create(user=self.user)
        response = self.client.get(reverse('api:account:user-profile'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'),
                         '{"type":"student-profile","id":%s}' % self.student_profile.id)


class MentorsListViewSetTest(TestCase):

    def test_status_OK(self):
        response = self.client.get(reverse('api:account:all-mentors-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '[]')
