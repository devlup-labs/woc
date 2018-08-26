from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class StudentProfile(models.Model):
    roll = RegexValidator(r'^[BMP][0-9]{2}[A-Z]{2}[0-9]{3}')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=8, validators=[roll])


class MentorProfile(models.Model):
    roll = RegexValidator(r'^[BMP][0-9]{2}[A-Z]{2}[0-9]{3}')
    name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=8, validators=[roll])
