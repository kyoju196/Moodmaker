from django.shortcuts import render, redirect

# Create your views here.

from django.views import generic

class camera(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'camera.html'
        return render(request, template_name)