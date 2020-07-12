from django.urls import include, path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'information'

urlpatterns = [
   path('', views.post_list, name='information'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
