from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Postagem, Resposta, Usuario
from .serializers import (PostagemSerializer, RespostaSerializer,
                          UsuarioSerializer)


class Usuario_ViewSet(viewsets.ModelViewSet): 
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class Postagem_ViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    
    
class Resposta_ViewSet(viewsets.ModelViewSet):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer
    
    
    @action(detail=True, methods=["get"], url_path=r'votar',)
    def votar(self, request, pk=None):
        print("Teste")
        object = Resposta.objects.get(pk=pk)
        object.votar()