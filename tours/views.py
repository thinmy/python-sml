from rest_framework import viewsets
from tours.models import Tour
from tours.serializers import TourSerializer


class TourViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint thats allow users to list all available categories
    """
    queryset = Tour.objects.is_active()
    serializer_class = TourSerializer
