from django.db import models
# from core.models import Contrato


class Material(models.Model):
    TIPO = (
        ("u", "Unidade"),
        ("m", "Metros"),
        ("o", "Outro")
    )
    numero_item = models.IntegerField()
    descricao = models.CharField(max_length=255)
    tipo_unidade = models.CharField(max_length=1, choices=TIPO)
    quantidade_ano = models.IntegerField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    comentarios = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='imagem_material', blank=True, null=True)

    # def material_imposto(self):
    #     contrato = Contrato.objects.get(id=1)
    #     total = self.valor * contrato.bdi
    #     return round(total, 2)

    def __str__(self):
        return str(self.numero_item) + ' - ' + str(self.descricao)


class Estoque(models.Model):
    name = models.CharField(max_length=50)
    material = models.ForeignKey(Material, models.SET_NULL, blank=True, null=True)
    fabricante = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=50, blank=True, null=True)
    desenho = models.CharField(max_length=50, blank=True, null=True)
    data_entrada = models.DateTimeField()
    localizacao = models.CharField(max_length=100, blank=True, null=True)
    data_saida = models.DateTimeField(blank=True, null=True)
    responsavel_retirada = models.CharField(max_length=50, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    em_estoque = models.BooleanField()

    def __str__(self):
        return str(self.material) + "-" + str(self.fabricante) + '-' + str(self.modelo)