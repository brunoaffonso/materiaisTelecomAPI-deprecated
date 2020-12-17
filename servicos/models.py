from django.db import models
from core.models import Unidade, Departamento, Setor
from materiais.models import Material
# from core.models import Contrato
# from django.db.models import Sum
# from django.db.models import F
# from django.db.models import FloatField
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from decimal import Decimal


class Servico(models.Model):
    numero_rs = models.IntegerField()
    numero_os = models.IntegerField()
    data_abertura = models.DateField(blank=True, null=True)
    data_fechamento = models.DateField(blank=True, null=True)
    unidade = models.ForeignKey(Unidade, models.SET_NULL, blank=True, null=True)
    departamento = models.ForeignKey(Departamento, models.SET_NULL, blank=True, null=True)
    setor = models.ForeignKey(Setor, models.SET_NULL, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    custo = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    # def total_servico(self):
    #     total = self.matserv_set.all().aggregate(
    #         total_rs=Sum(F('quantidade') * F('material__valor'), output_field=FloatField()))['total_rs']
    #
    #     # total2 = self.matserv_set.all().annotate(
    #     #     total_rs=Sum(F('quantidade') * F('material__valor'), output_field=FloatField()))['total_rs']
    #
    #     total_imposto = total * Contrato.bdi_atual(self.data_abertura)
    #     self.custo = Decimal.from_float(total_imposto)
    #     self.save()

    def __str__(self):
        return str(self.numero_rs) + ' - ' + str(self.data_abertura) + ' - ' + str(self.unidade)


class MatServ(models.Model):
    numero_rs = models.ForeignKey(Servico, models.SET_NULL, blank=True, null=True)
    material = models.ForeignKey(Material, models.SET_NULL, blank=True, null=True)
    quantidade = models.IntegerField()
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.numero_rs) + ' - ' + str(self.material)


# @receiver(post_save, sender=MatServ)
# def salva_valor_servico(sender, instance, **kwargs):
#     instance.numero_rs.total_servico()