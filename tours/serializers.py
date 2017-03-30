from rest_framework import serializers
from tours.models import Tour


class TourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tour
        fields = ('active', 'category', 'name', 'type', 'created_at')
