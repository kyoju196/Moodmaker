from django.conf.urls import include, url
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'information'

urlpatterns = [
   url(r'^$', views.information.as_view(), name='information'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
