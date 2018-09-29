from django.test import TestCase
from django.shortcuts import reverse
from rest_framework import status
from django.contrib.auth.models import User

from account.models import StudentProfile, MentorProfile
from project.models import Project


class ProjectViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.student = User.objects.create_user(username='student', email='student@test.com', password='password')
        cls.mentor = User.objects.create_user(username='mentor', email='mentor@test.com', password='password')
        cls.student_profile = StudentProfile.objects.create(user=cls.student, phone='9999999999',
                                                            github='https://github.com',
                                                            year=StudentProfile.YEAR_CHOICES[0][0],
                                                            gender=StudentProfile.GENDER_CHOICES[0][0],
                                                            branch=StudentProfile.BRANCH_CHOICES[0][0])
        cls.mentor_profile = MentorProfile.objects.create(user=cls.mentor, phone='9999999999',
                                                          github='https://github.com',
                                                          gender=StudentProfile.GENDER_CHOICES[0][0])

    def test_status_OK(self):
        response = self.client.get(reverse('api:project:projects-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), '[]')

    def test_create(self):
        data = {
            'name': 'Project 2',
            'github_link': 'https://github.com',
            'short_description': 'Short description',
            'description': 'Description',
            'technologies': 'Python,Django,C++',
            'mentors': [self.mentor_profile.id]
        }
        response = self.client.post(reverse('api:project:projects-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.login(username=self.mentor.username, password='password')
        response = self.client.post(reverse('api:project:projects-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.mentor_profile.is_approved = True
        self.mentor_profile.save()
        response = self.client.post(reverse('api:project:projects-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Project.objects.filter(name='Project 2', mentors='{}'.format(self.mentor_profile.id)).exists())
