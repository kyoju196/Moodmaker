from django.urls import include, path
from . import views

from django.conf import settings

app_name = 'home'

urlpatterns = [
   path('', views.home.as_view(), name='home'),
]

