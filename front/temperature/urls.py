from django.conf.urls import include, url
from . import views

from django.conf import settings
from django.conf.urls.static import static


app_name = 'temperature'

urlpatterns = [
   url(r'^$', views.temperature.as_view(), name='temperature'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
