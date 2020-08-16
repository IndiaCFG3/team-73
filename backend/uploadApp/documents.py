from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Centre,Employee

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
        related_models = [Employee,]