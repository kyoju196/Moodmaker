from django.shortcuts import render, redirect

# Create your views here.

from django.views import generic

class home(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'home.html'
        return render(request, template_name)