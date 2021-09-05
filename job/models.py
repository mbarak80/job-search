from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from accounts.models import City
from django.urls import reverse
import uuid
from .utils import generate_unique_slug




class City_Job(models.Model):
    city = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = ("City")
        verbose_name_plural = ("Job City")

    def __str__(self):
        return self.city

JOB_TYPE = (
    ('full-time', 'full-time'),
    ('part-time', 'part-time'),
)







class Job(models.Model):

    title           = models.CharField(max_length=100)
    job_type        = models.CharField(max_length=100, choices= JOB_TYPE)
    description     = models.TextField(max_length=1000)
    published_at    = models.DateTimeField(auto_now=True)
    categories      = models.ForeignKey('Category', verbose_name=("Category"), on_delete=models.CASCADE, null=True)
    vacancy         = models.IntegerField(default=1)
    salary          = models.IntegerField(default=0)
    experience      = models.IntegerField(default=1)
    city            = models.ForeignKey(City_Job, on_delete=models.CASCADE, null=True)
    slug            = models.SlugField(blank=True, null=True, unique=True)

    class Meta:
        ordering = ['-published_at']


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Job, self.title)
        else:  # create
            self.slug = generate_unique_slug(Job, self.title)
        super(Job, self).save(*args, **kwargs)




class Category(models.Model):
    cat_name = models.CharField(max_length=250, null=True)
    cat_job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)
    

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.cat_name
        

class Candidate(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    job             = models.ForeignKey(Job, related_name='Apply_job', on_delete=models.CASCADE)
    name            = models.CharField(max_length=100)
    email           = models.EmailField()
    url             = models.URLField()
    cv              = models.FileField(upload_to="Apply/")
    cover_letter    = models.TextField(max_length=1000)
    description     = models.TextField(max_length=1000, null=True)
    created         = models.DateTimeField(auto_now=True)
    job_name        = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name



class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    url = models.URLField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    




class Resume(models.Model):
    candidate = models.ForeignKey(Candidate, related_name='Resume', on_delete=models.CASCADE, blank=True, null=True )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    url = models.URLField()
    cv = models.FileField(upload_to="Apply/")
    cover_letter = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Companie(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    url = models.URLField()
    image   = models.ImageField(upload_to='Company/', blank=True, null=True)

    def __str__(self):
        return self.name






