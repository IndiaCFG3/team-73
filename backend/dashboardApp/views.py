from django.shortcuts import render
from django.http import HttpResponse

from.csv_parser import centre_csv_parser
# Create your views here.
def index(request):
    user = request.user
    group = user.groups.get()
    return HttpResponse(group)

def upload_centers(request):
    path='/datasets/Center.csv'
    centre_csv_parser("",path)