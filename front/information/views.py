from django.shortcuts import render, redirect
from django.views import generic

from django.http import HttpResponse, JsonResponse
import requests
from .models import Information
import json

# class information(generic.TemplateView):
#     def get(self, request, *args, **kwargs):
#         template_name = 'information.html'
#         return render(request, template_name)

def post_list(request):
    writing = Information.objects.all()
    data = requests.get('http://127.0.0.1:8080/information_restful').json()
    return JsonResponse(data, safe=False)