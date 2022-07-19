from os import sep
from re import sub
from django.db.models import query
from django.shortcuts import render
from publicararte.serializers import UserSerializer
from publicararte.models import Arte,Categoria,Tematica,Tags
from publicararte.serializers import ArteSerializer,TagsSerializer,TematicaSerializer,CategoriaSerializer
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from publicararte.permissions import IsArtista
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArteViewSet(viewsets.ModelViewSet):
    queryset = Arte.objects.all()
    serializer_class = ArteSerializer
    parser_class = (FormParser,MultiPartParser) 
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        if IsArtista.has_permission(self, request, view=ArteViewSet):
            self.request.data['tags'] = self.request.data['tags'][1:-1]
            print(self.request.data['tags'])
            #self.request.data['tags'] = self.request.data['tags'].split(sep=',')
            array = self.request.data['tags'].split(sep=',')
            self.request.data['tags'] = array[0]
            print(self.request.data['tags'])
            print(self.request.data)
            response = super(ArteViewSet, self).create(request, *args, **kwargs)
            # response.data has everything specified in your serializer; it seems fine to clobber it
            # alternatively, you could add to it: response.data['foo']='baz'
            response.data = {'id_url': f'{response.data["id"]}'}
            print(response.data)
            return response
        else:
            content = {'acesso': 'Você não é artista'}
            return Response(content)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
       
class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer 
       
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
             
class TematicaViewSet(viewsets.ModelViewSet):
    queryset = Tematica.objects.all()
    serializer_class = TematicaSerializer
       
