from .serializers import MaterialSerizlizer
from .serializers import EstoqueSerializer
from .serializers import ShortMaterialSerizlizer
from .serializers import ShortEstoqueSerializer
from .models import Material, Estoque
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerizlizer

    def list(self, request, *args, **kwargs):
        queryset = Material.objects.all()
        serializer = ShortMaterialSerizlizer(queryset, many=True)
        return Response(serializer.data)


class EstoqueViewSet(ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer

    def list(self, request, *args, **kwargs):
        queryset = Estoque.objects.all()
        serializer = ShortEstoqueSerializer(queryset, many=True)
        return Response(serializer.data)