from django.shortcuts import render
from django.views.generic import TemplateView


def page_func(request):
    return render(request, 'second_task/func_templates.html')


# Create your views here.

class page_class(TemplateView):
    template_name = ('second_task/class_templates.html')
