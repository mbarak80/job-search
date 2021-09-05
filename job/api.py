from .serializers import JobSerializer
from rest_framework import generics
from .models import Job




class JobApi(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer