from .models import information_board
from rest_framework import serializers

class Information_boardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = information_board
        fields = ('no', 'title', 'content')