from django.shortcuts import render

# Create your views here.

def TemperatureView(request):
    return render(request, 'temperature.html')