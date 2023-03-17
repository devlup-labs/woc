from django.contrib import admin
from .models import Project, StudentManual, MentorManual


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    class Meta:
        model = Project
        fields = '__all__'

@admin.register(StudentManual)
class StudentManualAdmin(admin.ModelAdmin):
    class Meta:
        model = StudentManual
        fields = '__all__'

@admin.register(MentorManual)
class MentorManualAdmin(admin.ModelAdmin):
    class Meta:
        model = MentorManual
        fields = '__all__'