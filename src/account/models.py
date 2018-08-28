from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class StudentProfile(models.Model):
    # Validators
    phone_validator = RegexValidator(r'^[0-9]{10}', message='Not a Valid Phone Number')
    # Choices
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    BRANCH_CHOICES = (
        ('CSE', 'Computer Science and Engineering'),
        ('EE', 'Electrical Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('BB', 'BioScience and BioTechnology')
    )
    YEAR_CHOICES = (
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
        ('4', '4th Year')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, validators=[phone_validator])
    github = models.URLField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    branch = models.CharField(max_length=3, choices=BRANCH_CHOICES)
    year = models.CharField(max_length=1, choices=YEAR_CHOICES, default=YEAR_CHOICES[0])


class MentorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
