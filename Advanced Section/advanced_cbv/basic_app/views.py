from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from  . import models
#from django.http import HttpResponse

# Original Function View:
#
# def index(request):
#     return render(request,'index.html')

class IndexView(TemplateView):
    # template_name = 'app_name/site.html'
    template_name = 'index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'basic_app/school_detail.html'
