from rest_framework.serializers import ModelSerializer
from .models import Unidade, Departamento, Setor, Contrato


class UnidadeSerizlizer(ModelSerializer):
    class Meta:
        model = Unidade
        fields = ['name']


class DepartamentoSerializer(ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['name', 'unidade']


class SetorSerializer(ModelSerializer):
    class Meta:
        model = Setor
        fields = ['name', 'departamento']


class ContratoSerializer(ModelSerializer):
    class Meta:
        model = Contrato
        fields = ['numero',
                  'ano',
                  'renovacao',
                  'inicio',
                  'fim',
                  'bdi',
                  'descricao']


class ShortContratoSerializer(ModelSerializer):
    class Meta:
        model = Contrato
        fields = ['numero',
                  'ano',
                  'descricao',
                  'fim']