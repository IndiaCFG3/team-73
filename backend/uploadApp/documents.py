from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Centre,Employee, Student, Course

@registry.register_document
class CentreDocument(Document):
    hod = fields.ObjectField(properties={
        'name': fields.TextField(),
        'designation' : fields.TextField(),
        'rating': fields.IntegerField(),
        'salary' : fields.IntegerField(),
        'on_sabbatical': fields.BooleanField(),
        'number_of_leaves': fields.IntegerField(),
    })
    class Index :
        name = 'centres'

    class Django :
        model = Centre
        fields = [
            'name',
            'rating',
            'city',
            'state',
            'location',
        ]


@registry.register_document
class EmployeeDocument(Document):
    class Index :
        name = 'yuvaparivartan-employee'

    class Django :
        model = Employee
        fields = [
            'name',
            'designation',
            'rating',
            'salary',
            'on_sabbatical',
            'number_of_leaves',
        ]

@registry.register_document
class StudentDocument(Document):
    centre = fields.ObjectField(properties={
        'name': fields.TextField(),
        'rating': fields.IntegerField(),
        'city' : fields.TextField(),
        'state': fields.TextField(),
        'location': fields.TextField(),
    })
    class Index :
        name = 'yuvaparivartan-student'

    class Django :
        model = Student
        fields = [
            'name',
            'dob',
            'attendance',
            'batch',
            'paid_fees',
            'passed',
            'placed',
        ]