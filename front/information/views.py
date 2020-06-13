from django.shortcuts import render, redirect
import requests

from django.http import HttpResponse, JsonResponse

# Create your views here.

from django.views import generic

class information(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'information.html'
        return render(request, template_name)

def post_list3(request):
    return JsonResponse({
        'message' : '안녕 파이썬 장고',
        'items' : ['파이썬', '장고', 'AWS', 'Azure'],
    }, json_dumps_params = {'ensure_ascii': True})