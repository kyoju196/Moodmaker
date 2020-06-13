from django.conf.urls import include, url
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

urlpatterns = [
   url(r'^$', views.home.as_view(), name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
