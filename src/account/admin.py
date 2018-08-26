from django.contrib import admin
from .models import StudentProfile, MentorProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = StudentProfile
        fields = '__all__'


@admin.register(MentorProfile)
class MentorProifileAdmin(admin.ModelAdmin):
    class Meta:
        model = MentorProfile
        fields = '__all__'
