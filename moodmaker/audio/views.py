from django.shortcuts import render

# Create your views here.

def AudioView(request):
    return render(request, 'audio.html')