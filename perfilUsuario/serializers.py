from perfilUsuario.models import Perfil
from rest_framework import serializers

from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from rest_framework.authtoken.models import Token

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['user', 'is_artista']


class NameRegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.save(update_fields=['first_name', 'last_name'])

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user')
