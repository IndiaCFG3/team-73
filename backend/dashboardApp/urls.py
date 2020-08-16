from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name='dashboard'),
    path('upload-centers/',views.upload_centers , name='upload_centers'),
]