from rest_framework import routers
from categories import views

'''
Generates rest_framework routes for Categories
'''
router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
