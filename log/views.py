from django.shortcuts import render
from rest_framework import viewsets
from log.models import Log
from log.serializers import LogSerializer

# Create your views here.
class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer 