from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from core.models import Categoria
from core.serializers import CategoriaSerializer


class CategoriasLisGeneric(ListCreateAPIView):
    """
    Já está implementado os métodos get e post
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    lookup_field = 'id'
