from django.db import models


class Unidade(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Departamento(models.Model):
    name = models.CharField(max_length=30)
    unidade = models.ForeignKey(Unidade, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.unidade) + ' - ' + str(self.name)


class Setor(models.Model):
    name = models.CharField(max_length=30)
    departamento = models.ForeignKey(Departamento, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Contrato(models.Model):
    RENOVACAO = (
        ("0", "Primeiro ano de Contrato"),
        ("1", "1 Renovação"),
        ("2", "2 Renovações"),
        ("3", "3 Renovações"),
        ("4", "4 Renovações"),
    )
    numero = models.IntegerField()
    ano = models.IntegerField()
    renovacao = models.CharField(max_length=1, choices=RENOVACAO)
    inicio = models.DateField()
    fim = models.DateField()
    bdi = models.DecimalField(max_digits=8, decimal_places=6)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    # def bdi_atual(self):
    #     atual = Contrato.objects.filter(inicio__lte=self).values_list('bdi', flat=True)[0]
    #     return float(atual)
    #
    def __str__(self):
        return str(self.numero)+ ' / ' + str(self.ano) + ' - ' + str(self.periodo)