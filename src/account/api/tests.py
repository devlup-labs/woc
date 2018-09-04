from django.test import TestCase
from django.shortcuts import reverse
from rest_framework import status
from account.models import StudentProfile
from account.models import MentorProfile
from django.contrib.auth.models import User

WRONG_PHONE = (
    99999,
    'ABC',
    99999999999

)

WRONG_BRANCH = (
    'AB',
    'ABCD'
)

class StudentProfileCreateTest(TestCase):
    @classmethod

    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='student', password='password')




    def test_bad_request(self):
        response = self.client.post(reverse('api:account:student-profile-list'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,'Error: Wrong response[User entered no data]')

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
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,'Error : Wrong response[Error in creation of user]')

    def test_missing_userid(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': StudentProfile.GENDER_CHOICES[0][0],
            'branch': StudentProfile.BRANCH_CHOICES[0][0],
            'year': StudentProfile.YEAR_CHOICES[0][0],
        }
        response = self.client.post(reverse('api:account:student-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST,'Error : Wrong response[Missing user id]')

    def test_invalid_userid(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': StudentProfile.GENDER_CHOICES[0][0],
            'branch': StudentProfile.BRANCH_CHOICES[0][0],
            'year': StudentProfile.YEAR_CHOICES[0][0],
            'user': self.user.id + 12
        }
        response = self.client.post(reverse('api:account:student-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST,'Error : Wrong response[Invalid user id]')



    """def test_phone_short(self):
        data = {
            'phone': WRONG_PHONE[0], # shorter than 10 digits
            'github': 'https://github.com/abc',
            'gender': StudentProfile.GENDER_CHOICES[0][0],
            'branch': StudentProfile.BRANCH_CHOICES[0][0],
            'year': StudentProfile.YEAR_CHOICES[0][0],
            'user': self.user.id
        }
        response = self.client.post(reverse('api:account:student-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_phone_invalid(self):
        data = {
            'phone': WRONG_PHONE[1], #abcd
            'github': 'https://github.com/abc',
            'gender': StudentProfile.GENDER_CHOICES[0][0],
            'branch': StudentProfile.BRANCH_CHOICES[0][0],
            'year': StudentProfile.YEAR_CHOICES[0][0],
            'user': self.user.id
        }
        response = self.client.post(reverse('api:account:student-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_phone_long(self):
        data = {
            'phone': WRONG_PHONE[2], #99999999999 longer thn 10 digits
            'github': 'https://github.com/abc',
            'gender': StudentProfile.GENDER_CHOICES[0][0],
            'branch': StudentProfile.BRANCH_CHOICES[0][0],
            'year': StudentProfile.YEAR_CHOICES[0][0],
            'user': self.user.id
        }
        response = self.client.post(reverse('api:account:student-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_branch_wrong(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': StudentProfile.GENDER_CHOICES[0][0],
            'branch': WRONG_BRANCH[0], #AB
            'year': StudentProfile.YEAR_CHOICES[0][0],
            'user': self.user.id
        }
        response = self.client.post(reverse('api:account:student-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_branch_long(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': StudentProfile.GENDER_CHOICES[0][0],
            'branch': WRONG_BRANCH[1], #abcd
            'year': StudentProfile.YEAR_CHOICES[0][0],
            'user': self.user.id
        }
        response = self.client.post(reverse('api:account:student-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_gender(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': 'B',
            'branch': WRONG_BRANCH[1],
            'year': StudentProfile.YEAR_CHOICES[0][0],
            'user': self.user.id
        }
        response = self.client.post(reverse('api:account:student-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)"""






class MentorProfileCreateTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='mentor', password='password')

    def test_bad_request(self):
        response = self.client.post(reverse('api:account:mentor-profile-list'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, 'Error: Wrong response[User entered no data]')

    def test_created(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': MentorProfile.GENDER_CHOICES[0][0],
            'branch': MentorProfile.BRANCH_CHOICES[0][0],
            'year': MentorProfile.YEAR_CHOICES[0][0],
            'user': self.user.id
        }
        response = self.client.post(reverse('api:account:mentor-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,'Error : Wrong response[Error in creation of user]')

    def test_missing_userid(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': MentorProfile.GENDER_CHOICES[0][0],
            'branch': MentorProfile.BRANCH_CHOICES[0][0],
            'year': MentorProfile.YEAR_CHOICES[0][0],
        }
        response = self.client.post(reverse('api:account:mentor-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, 'Error : Wrong response[Missing user id]')

    def test_invalid_userid(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': MentorProfile.GENDER_CHOICES[0][0],
            'branch': MentorProfile.BRANCH_CHOICES[0][0],
            'year': MentorProfile.YEAR_CHOICES[0][0],
            'user' : self.user.id + 12
        }
        response = self.client.post(reverse('api:account:mentor-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, 'Error : Wrong response[Invalid user id]')


    """def test_phone_short(self):
        data = {
            'phone': WRONG_PHONE[0],
            'github': 'https://github.com/abc',
            'gender': MentorProfile.GENDER_CHOICES[0][0],
            'branch': MentorProfile.BRANCH_CHOICES[0][0],
            'year': MentorProfile.YEAR_CHOICES[0][0],
            'user': self.user.id
        }
        response = self.client.post(reverse('api:account:mentor-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_phone_invalid(self):
        data = {
            'phone': WRONG_PHONE[1],
            'github': 'https://github.com/abc',
            'gender': MentorProfile.GENDER_CHOICES[0][0],
            'branch': MentorProfile.BRANCH_CHOICES[0][0],
            'year': MentorProfile.YEAR_CHOICES[0][0],
            'user': self.user.id
        }
        response = self.client.post(reverse('api:account:mentor-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_phone_long(self):
        data = {
            'phone': WRONG_PHONE[2],
            'github': 'https://github.com/abc',
            'gender': MentorProfile.GENDER_CHOICES[0][0],
            'branch': MentorProfile.BRANCH_CHOICES[0][0],
            'year': MentorProfile.YEAR_CHOICES[0][0],
            'user': self.user.id
        }
        response = self.client.post(reverse('api:account:mentor-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_branch_wrong(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': MentorProfile.GENDER_CHOICES[0][0],
            'branch': WRONG_BRANCH[0],
            'year': MentorProfile.YEAR_CHOICES[0][0],
            'user': self.user.id
        }
        response = self.client.post(reverse('api:account:student-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_branch_long(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': MentorProfile.GENDER_CHOICES[0][0],
            'branch': WRONG_BRANCH[1],
            'year': MentorProfile.YEAR_CHOICES[0][0],
            'user': self.user.id
        }
        response = self.client.post(reverse('api:account:student-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_gender(self):
        data = {
            'phone': 9999999999,
            'github': 'https://github.com/abc',
            'gender': 'B',
            'branch': WRONG_BRANCH[1],
            'year': MentorProfile.YEAR_CHOICES[0][0],
            'user': self.user.id
        }
        response = self.client.post(reverse('api:account:student-profile-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)"""


