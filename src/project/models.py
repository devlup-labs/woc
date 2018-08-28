from django.db import models
from account.models import StudentProfile, MentorProfile


class Project(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    github_link = models.URLField()
    # associations
    students = models.ManyToManyField(StudentProfile, through='Proposal', through_fields=('project', 'student'))
    mentors = models.ManyToManyField(MentorProfile)


class Proposal(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    drive_link = models.URLField()
    file = models.FileField(upload_to='proposals')
    is_accepted = models.BooleanField(default=False)
