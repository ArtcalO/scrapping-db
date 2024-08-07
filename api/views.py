from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import *

class ScrappedItemsViewSet(viewsets.ModelViewSet):
    queryset = ScrappedItems.objects.all()
    serializer_class = ScrappedItemsSerializer