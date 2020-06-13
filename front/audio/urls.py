from django.conf.urls import include, url
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'audio'

urlpatterns = [
   url(r'^$', views.audio.as_view(), name='audio'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
