
from django.contrib import admin
from django.urls import path, include,re_path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest_api/', include("api.urls")),
    path("graphql_api", include("graphql_api.urls")),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
