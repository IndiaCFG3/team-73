from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .csv_parser import employee_csv_parser, studnet_csv_parser, course_csv_parser, centre_csv_parser

def csvUploadView(request):
    content = None
    if request.method == 'POST' and request.FILES['content']:
        content = request.FILES['csv-content']
        fs = FileSystemStorage(location= '/temp')
        filename = fs.save(content.name,content)
    return render(request, '', {'content':content})
