from django.shortcuts import render
from perfilUsuario import serializers
from rest_framework import viewsets
from perfilUsuario.models import Perfil
from dj_rest_auth.registration.views import RegisterView
from perfilUsuario.serializers import PerfilSerializer, NameRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

from google.oauth2 import id_token
from google.auth.transport import requests

class VerifyTokenGoogle(APIView):
    def post(self, request):
        try:
            CLIENT_ID = '611769950969-4u73ggrkesk1hef91se02vbuig9tme3v.apps.googleusercontent.com'
            # Specify the CLIENT_ID of the app that accesses the backend:
            token = request.data['idtoken']
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
            # Or, if multiple clients access the backend server:
            # idinfo = id_token.verify_oauth2_token(token, requests.Request())
            # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
            #     raise ValueError('Could not verify audience.')
        
            # If auth request is from a G Suite domain:
            # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
            #     raise ValueError('Wrong hosted domain.')
        
            # ID token is valid. Get the user's Google Account ID from the decoded token.
            userid = idinfo['sub']
            return Response(userid)
        except ValueError:
            # Invalid token
            pass

# Create your views here.
class PerfilPostView(APIView):
    def post(self, request):
        serializer = PerfilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        lista_perfis = Perfil.objects.all()
        serializer = PerfilSerializer(lista_perfis, many=True)
        return Response(serializer.data)      

class NameRegistrationView(RegisterView):
    serializer_class = NameRegistrationSerializer

class PerfilInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    # Header = { 
    # Authorization: Token <token do user>
    # }

    def get(self, request):
        content = {
            'id': request.user.id,
            'username': f'{request.user}',
            'email': f'{request.user.email}',
            'first_name': f'{request.user.first_name}',
            'last_name': f'{request.user.last_name}',
            'is_artista': request.user.perfil.is_artista,
        }
        return Response(content)
