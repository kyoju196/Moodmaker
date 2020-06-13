from .models import information_board
from .serializers import Information_boardSerializer
from django.views import View
from django.views import generic
from rest_framework import viewsets

class Information_board_main(viewsets.ModelViewSet):
    queryset = information_board.objects.all()
    serializer_class = Information_boardSerializer