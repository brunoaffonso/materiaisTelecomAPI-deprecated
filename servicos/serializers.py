from rest_framework.serializers import ModelSerializer
from .models import Servico, MatServ

class ServicoSerializer(ModelSerializer):
    class Meta:
        model = Servico
        fields = ['numero_rs',
                  'numero_os',
                  'data_abertura',
                  'data_fechamento',
                  'unidade',
                  'departamento',
                  'setor',
                  'obs',
                  'custo']


class ShortServicoSerializer(ModelSerializer):
    class Meta:
        model = Servico
        fields = ['numero_rs',
                  'numero_os',
                  'data_abertura',
                  'data_fechamento',
                  'unidade',
                  'custo']


class MatServSerializer(ModelSerializer):
    class Meta:
        model = MatServ
        fields = ['numero_rs',
                  'material',
                  'quantidade',
                  'comentarios']


class ShortMatServSerializer(ModelSerializer):
    class Meta:
        model = MatServ
        fields = ['numero_rs',
                  'material',
                  'quantidade']