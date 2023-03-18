from django.db import models
from account.models import StudentProfile, MentorProfile


class Project(models.Model):
    name = models.CharField(max_length=64, help_text='Name of project')
    short_description = models.CharField(max_length=64, help_text='Short description of project')
    description = models.TextField(help_text='Description of project')
    github_link = models.URLField(help_text='Github link of the project')
    technologies = models.CharField(help_text='Technologies to be used in the project', max_length=2048)
    # associations
    students = models.ManyToManyField(StudentProfile, through='StudentProposal', through_fields=('project', 'student'),
                                      help_text='Students working on the project')
    mentors = models.ManyToManyField(MentorProfile, help_text='Mentors of the project')

    @property
    def technologies_as_list(self):
        if self.technologies == '' or not self.technologies:
            return ['']
        return self.technologies.split('|')

    def __str__(self):
        return self.name


class StudentProposal(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, help_text='Proposal for the project')
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, help_text='Name of the student proposed')
    drive_link = models.URLField(help_text='Custom drive link for proposal')
    file = models.FileField(upload_to='proposals', null=True, blank=True, help_text='File link')
    is_accepted = models.BooleanField(default=False, help_text='Accepted/Rejected')

    class Meta:
        unique_together = (('project', 'student'),)

    def __str__(self):
        return self.student.user.get_full_name() + " | " + self.project.name

class StudentManual(models.Model):
    manual = models.FileField(upload_to='manuals', null=True, blank=True, help_text='File link')

class MentorManual(models.Model):
    manual = models.FileField(upload_to='manuals', null=True, blank=True, help_text='File link')
