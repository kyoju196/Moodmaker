from django.conf.urls import include, url
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'camera'

urlpatterns = [
   url(r'^$', views.camera.as_view(), name='camera'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
