from django.shortcuts import render
from django.views.generic import TemplateView
def page_func(request):
    return render(request, 'func_templates.html')
# Create your views here.

class page_class(TemplateView):
    template_name = ('class_templates.html')

