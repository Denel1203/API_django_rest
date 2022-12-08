from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.CharField(max_length=3)
    rg = models.CharField(max_length=7)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome
    
    
class Postagem(models.Model):
    usuario = models.ForeignKey(Usuario, null=True,
                                on_delete=models.CASCADE )
    titulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=1000)
    def __str__(self):
        return self.titulo
    
  
  
class Resposta(models.Model):
    usuario = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE )
    postagem = models.ForeignKey(Postagem, null=True, on_delete=models.CASCADE )
    voto = models.IntegerField(default=0, blank=False, null=False)
    descriçao = models.CharField(max_length=30)
    comentario = models.TextField(max_length=500)

    def __str__(self):
        return self.descriçao
    
    def votar(self):
        self.voto += 1
        if self.save():
            return True
        return False
        
   
    
      
   