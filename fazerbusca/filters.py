from dataclasses import fields
from django_filters import rest_framework as filters
from publicararte.models import *


class ArtFilter(filters.FilterSet):
    nome = filters.CharFilter(field_name='nome', lookup_expr='icontains')
    descricao = filters.CharFilter(
        field_name='descricao', lookup_expr='icontains')
    preco = filters.CharFilter(field_name='preco', lookup_expr='icontains')
    formato = filters.CharFilter(field_name='formato', lookup_expr='icontains')

    class Meta:
        model = Arte
        fields = ('nome', 'descricao', 'preco', 'formato',)
