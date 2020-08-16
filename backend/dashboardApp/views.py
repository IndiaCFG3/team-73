from django.shortcuts import render,redirect
from django.http import HttpResponse

from.csv_parser import centre_csv_parser
# Create your views here.
def index(request):
    user = request.user
    group = user.groups.get()
    return render(request,'dashboard/dashboard.html',{
        'user': user,
        'group': group,
    })

def upload_centers(request):
    path='/tmp/Center.csv'
    centre_csv_parser("",path)
    return redirect('/api/admin/')