from django.shortcuts import render
from django.views.generic import View, TemplateView
#from django.http import HttpResponse

# Original Function View:
#
# def index(request):
#     return render(request,'index.html')

class IndexView(TemplateView):
    # template_name = 'app_name/site.html'
    template_name = 'index.html'


class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')
