from .serializers import ServicoSerializer
from .serializers import ShortServicoSerializer
from .serializers import MatServSerializer
from .serializers import ShortMatServSerializer
from .models import Servico, MatServ
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class ServicoViewSet(ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

    def list(self, request, *args, **kwargs):
        queryset = Servico.objects.all()
        serializer = ShortServicoSerializer(queryset, many=True)
        return Response(serializer.data)


class MatServViewSet(ModelViewSet):
    queryset = MatServ.objects.all()
    serializer_class = MatServSerializer

    def list(self, request, *args, **kwargs):
        queryset = MatServ.objects.all()
        serializer = ShortMatServSerializer(queryset, many=True)
        return Response(serializer.data)

