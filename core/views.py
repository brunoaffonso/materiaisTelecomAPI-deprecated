from .serializers import UnidadeSerizlizer
from .serializers import DepartamentoSerializer
from .serializers import SetorSerializer
from .serializers import ContratoSerializer
from .serializers import ShortContratoSerializer
from .models import Unidade, Departamento, Setor, Contrato
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import render


class UnidadeViewSet(ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerizlizer


class DepartamentoViewSet(ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class SetorViewSet(ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer


class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    # permission_classes = [IsAuthenticated]
    #authentication_classes = (TokenAuthentication,)

    def list(self, request, *args, **kwargs):
        queryset = Contrato.objects.all()
        serializer = ShortContratoSerializer(queryset, many=True)
        return Response(serializer.data)
