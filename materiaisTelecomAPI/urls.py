"""materiaisTelecomAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import UnidadeViewSet, DepartamentoViewSet, SetorViewSet, ContratoViewSet
from materiais.views import MaterialViewSet, EstoqueViewSet
from servicos.views import ServicoViewSet, MatServViewSet

router = routers.DefaultRouter()
router.register(r'core/unidade', UnidadeViewSet)
router.register(r'core/departamento', DepartamentoViewSet)
router.register(r'core/setor', SetorViewSet)
router.register(r'core/contrato', ContratoViewSet)
router.register(r'materiais', MaterialViewSet)
router.register(r'estoque', EstoqueViewSet)
router.register(r'servico', ServicoViewSet)
router.register(r'matserv', MatServViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
