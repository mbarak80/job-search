from django import forms

from .models import Candidate, Job, Candidate, Resume, User




class JobForm(forms.ModelForm):
    title               = forms.CharField(max_length=200, widget=forms.TextInput({ "placeholder": ""}))



    class Meta:
        model = Job
        fields = ['title', 'description', 'job_type', 'vacancy','salary', 'experience', 'city']


class ResumeForm(forms.ModelForm):
    name          = forms.CharField(max_length=200, widget=forms.TextInput({"placeholder": ""}))
    email         = forms.EmailField(max_length=200, widget=forms.TextInput({ "placeholder": ""}))
    url           = forms.URLField(required=False, widget=forms.TextInput({ "placeholder": ""}))

    class Meta:
        model = Resume

        fields = ['name', 'email', 'url', 'cv', 'cover_letter']




class JobSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='Search Job!',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )

    

