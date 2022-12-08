from rest_framework import serializers

from .models import Postagem, Resposta, Usuario


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Usuario
        fields = ('id', 'url', 'nome', 'idade',
                  'rg', 'cpf', 'email', 'telefone' )


class PostagemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Postagem
        fields = ('id','usuario', 'titulo', 'texto', 'url')


class RespostaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Resposta
        fields = ('id','usuario', 'postagem', 'descriçao',
                  'voto', 'comentario', 'url')