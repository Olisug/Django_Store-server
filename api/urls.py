from django.urls import path, include
from rest_framework import routers
from api.views import ProductModelViewSet, CategoryModelViewSet, BasketModelViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'products_api', ProductModelViewSet)
router.register(r'categories_api', CategoryModelViewSet)
router.register(r'baskets_api', BasketModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
