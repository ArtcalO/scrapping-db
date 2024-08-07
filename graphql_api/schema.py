import graphene
from graphene_django import DjangoObjectType

from api.models import ScrappedItems

class ScrappedItemsType(DjangoObjectType):
    class Meta:
        model = ScrappedItems
        fields = ("adresse","title","prix","type_habitat","surface_habitable","nbr_pieces","description","dpe","ges","images","html_content")

class Query(graphene.ObjectType):
    all_scrapped_items = graphene.List(ScrappedItemsType)

    def resolve_all_scrapped_items(root, info):
        return ScrappedItems.objects.all()

schema = graphene.Schema(query=Query)