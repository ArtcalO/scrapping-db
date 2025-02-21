from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register("scrapped-items", ScrappedItemsViewSet)
router.register("test", TestPositiveBingIntegerViewSet)

urlpatterns = [
    path('',include(router.urls)),
]