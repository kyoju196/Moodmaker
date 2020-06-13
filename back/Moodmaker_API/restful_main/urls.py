from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'information_board', views.Information_board_main)

urlpatterns = [
    url(r'^$', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls')),
]