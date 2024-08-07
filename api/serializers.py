from rest_framework import serializers
from .models import *
class ScrappedItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrappedItems
        fields = "__all__"