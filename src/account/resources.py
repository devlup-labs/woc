from import_export import resources,fields
from project.models import StudentProposal
class StudentProposalResource(resources.ModelResource):
    project_mentors = fields.Field(column_name='Mentor', attribute='get_project_mentors')
    student__user__username = fields.Field(column_name='Student Name', attribute='student__user__username')
    student__user__email = fields.Field(column_name='Email', attribute='student__user__email')
    student__year = fields.Field(column_name='Year', attribute='student__year')
    project__name = fields.Field(column_name='Project Name', attribute='project__name')
    drive_link = fields.Field(column_name='Drive Link', attribute='drive_link')
    proposalStatus = fields.Field(column_name='Proposal Status', attribute='proposalStatus')

    class Meta:
        model = StudentProposal
        fields = ('student__user__username', 'student__user__email', 'student__year', 'project__name', 'project_mentors', 'drive_link', 'proposalStatus')
        export_order = ( 'student__user__username', 'student__user__email', 'student__year', 'project__name', 'project_mentors', 'drive_link', 'proposalStatus')

    def dehydrate_project_mentors(self, student_proposal):
        mentors = student_proposal.project.mentors.all()        
        mentor_names = ', '.join([mentor.user.get_full_name() for mentor in mentors])

        return mentor_names
    
    def get_queryset(self):
        return super(StudentProposalResource, self).get_queryset().order_by('student__year')
    

    
