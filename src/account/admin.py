from django.contrib import admin
from .models import StudentProfile, MentorProfile
from project.models import StudentProposal
from import_export.admin import ImportExportModelAdmin
from .resources import StudentProposalResource


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
class StudentProposalAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = StudentProposalResource
    list_display = ('student', 'project','drive_link', 'proposalStatus',)
    list_filter = ('project__name', 'student__user__username', 'proposalStatus',)
    search_fields = ['student__user__username',]

    class Meta:
        model = StudentProposal
        fields = '__all__'
