from rest_framework.serializers import ModelSerializer
from .models import Material, Estoque


class MaterialSerizlizer(ModelSerializer):
    class Meta:
        model = Material
        fields = ['numero_item',
                  'descricao',
                  'tipo_unidade',
                  'quantidade_ano',
                  'valor',
                  'comentarios',
                  'imagem']


class ShortMaterialSerizlizer(ModelSerializer):
    class Meta:
        model = Material
        fields = ['numero_item',
                  'descricao']


class EstoqueSerializer(ModelSerializer):
    class Meta:
        model = Estoque
        fields = ['name',
                  'material',
                  'fabricante',
                  'modelo',
                  'numero_serie',
                  'desenho',
                  'data_entrada',
                  'localizacao',
                  'data_saida',
                  'responsavel_retirada',
                  'info',
                  'em_estoque']


class ShortEstoqueSerializer(ModelSerializer):
    class Meta:
        model = Estoque
        fields = ['name', 'material',
                  'fabricante',
                  'modelo',
                  'data_entrada',
                  'localizacao',
                  'data_saida',
                  'em_estoque']