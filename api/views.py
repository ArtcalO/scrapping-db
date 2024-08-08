from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import *
from rest_framework.response import Response

class ScrappedItemsViewSet(viewsets.ModelViewSet):
    queryset = ScrappedItems.objects.all()
    serializer_class = ScrappedItemsSerializer

    def create(self, request):
        data = request.data
        adresse = data['adresse']
        title = data['title']
        prix = data['prix']
        type_habitat = data['type_habitat']
        surface_habitable = data['surface_habitable']
        surface_terrain = data['surface_terrain']
        nbr_pieces = data['nbr_pieces']
        description = data['description']
        dpe = data['dpe']
        ges = data['ges']
        images = data['images']
        html_content = data['html_content']
        image_1 = request.FILES.get('file')

        ScrappedItems(
            adresse = adresse,
            title = title,
            prix = prix,
            type_habitat = type_habitat,
            surface_habitable = surface_habitable,
            surface_terrain = surface_terrain,
            nbr_pieces = nbr_pieces,
            description = description,
            dpe = dpe,
            ges = ges,
            images = images,
            html_content = html_content,
            image_1 = image_1
        ).save()
        return Response({"status":"Datat posted"},201)