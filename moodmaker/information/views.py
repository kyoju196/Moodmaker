from django.shortcuts import render

# Create your views here.

def InformationView(request):
    return render(request, 'information.html')