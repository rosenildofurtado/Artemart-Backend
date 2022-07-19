from publicararte.models import Tags, Categoria, Tematica, Arte
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    artes = serializers.PrimaryKeyRelatedField(many=True, queryset=Arte.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'artes', 'owner', 'email', 'perfil']

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['nome', 'id']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria

        fields = ['nome', 'id']


class TematicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tematica
        fields = ['nome', 'id']


class ArteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arte
        fields = ['nome', 'descricao', 'formato', 'owner', 'tags', 'preco', 'foto', 'tematica',
                  'categoria', 'aprovado', 'id', 'image_width', 'image_height', 'slug']
