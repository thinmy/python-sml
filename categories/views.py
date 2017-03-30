from django.shortcuts import render
from rest_framework import viewsets

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint thats allow users to list all available categories
    '''
    queryset = Category.objects.is_active()
    serializer_class = CategorySerializer
