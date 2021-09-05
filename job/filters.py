import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='title')


    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['description', 'image', 'salary', 'published_at', 'vacancy', 'country', 'slug', 'experience']


