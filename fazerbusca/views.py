
from django.shortcuts import render
from publicararte.models import Arte
from publicararte.serializers import *
from rest_framework.parsers import FormParser, MultiPartParser


from rest_framework import viewsets
from fazerbusca.filters import ArtFilter
# Create your views here.

class ArteViewSet(viewsets.ModelViewSet):
    queryset = Arte.objects.all()
    serializer_class = ArteSerializer
    filterset_class = ArtFilter

    