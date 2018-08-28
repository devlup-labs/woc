from django.db import models
from uuid import uuid4
from account.models import StudentProfile, MentorProfile


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4())
    Name = models.CharField(max_length=50)
    student = models.ManyToManyField(StudentProfile)
    mentor = models.ManyToManyField(MentorProfile)
    Description = models.TextField()
    Github_link = models.URLField()
