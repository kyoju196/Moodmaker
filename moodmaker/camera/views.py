from django.shortcuts import render

# Create your views here.

def CameraView(request):
    return render(request, 'camera.html')