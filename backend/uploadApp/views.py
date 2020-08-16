from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage


def csvUploadView(request):
    if request.method == 'POST' and request.FILES['content']:
        content = request.FILES['csv-content']
        fs = FileSystemStorage(location= '/temp')
        filename = fs.save(content.name,content)

    return redirect('/api/dashboard/upload_centers')
