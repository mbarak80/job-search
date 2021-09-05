from django.urls import path
from .views import job_list, job_details, home, add_job, upload_resume

from . import api


 

app_name = 'job'

urlpatterns = [

    path('', home, name='index'),
    path('jobs/', job_list, name='home'),
    path('upload_resume/', upload_resume, name='upload_resume'),
    path('add_job', add_job, name='add_job'),
    path('<slug:slug>', job_details, name='job_details'),



    path('api/jobs',api.JobApi.as_view() , name='job_list_api'),

    
    

]


