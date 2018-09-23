from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class BaseProfile(models.Model):
    # Validators
    phone_validator = RegexValidator(r'^[6-9][0-9]{9}', message='Not a Valid Phone Number')
    # Choices
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, validators=[phone_validator], help_text='10 digit mobile number')
    github = models.URLField(help_text='Github link of user')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, help_text='Gender')

    class Meta:
        abstract = True


class StudentProfile(BaseProfile):
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
    branch = models.CharField(max_length=3, choices=BRANCH_CHOICES, help_text='Department of the user')
    year = models.CharField(max_length=1, choices=YEAR_CHOICES, help_text='Year of studying')


class MentorProfile(BaseProfile):
    is_approved = models.BooleanField(default=False)
