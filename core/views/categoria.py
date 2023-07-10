from core.models import Categoria
from rest_framework import viewsets
from core.serializers import CategoriaSerializer


class CategoriaViewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
