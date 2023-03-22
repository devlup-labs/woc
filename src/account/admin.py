from django.contrib import admin
from .models import StudentProfile, MentorProfile
from project.models import StudentProposal


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = StudentProfile
        fields = '__all__'


@admin.register(MentorProfile)
class MentorProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = MentorProfile
        fields = '__all__'


@admin.register(StudentProposal)
class StudentProposalAdmin(admin.ModelAdmin):
    list_display = ('student', 'project','drive_link', 'is_accepted',)
    list_filter = ('project__name', 'student__user__username', 'is_accepted',)
    search_fields = ['student__user__username',]

    class Meta:
        model = StudentProposal
        fields = '__all__'
