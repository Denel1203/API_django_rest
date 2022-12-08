from django.test import TestCase

from blog.models import Postagem, Resposta, Usuario


class UsuarioTestCase(TestCase):
       
        
    def test_Equal_usuario_nome_idade_rg_cpf_email_telefone(self):
        
        usuario = Usuario.objects.create(
            nome = "daniel",     
            idade = "27",
            rg = "1234567",
            cpf = "12345678910",
            email = "daniel@gmail.com",
            telefone = "12345678"
        )
        
        usuario_result = Usuario.objects.last()
        
        self.assertEqual(usuario_result.nome, "daniel")
        self.assertEqual(usuario_result.idade, "27")
        self.assertEqual(usuario_result.rg, "1234567")
        self.assertEqual(usuario_result.cpf, "12345678910")
        self.assertEqual(usuario_result.email, "daniel@gmail.com")
        self.assertEqual(usuario_result.telefone, "12345678")
        #fim do usuario


        postagem = Postagem.objects.create(
            titulo = "vida",
            texto = "maria dos campos"        
        )
    
        postagem_result = Postagem.objects.last()
        
        self.assertEquals(postagem_result.titulo, "vida")
        self.assertEquals(postagem_result.texto, "maria dos campos")
        #fim da postagem
        
        resposta = Resposta.objects.create(
            voto = 7,
            descriçao = "otimo",
            comentario = "continue bem"
        )

        resposta_retorno = Resposta.objects.last()
        self.assertEquals(resposta_retorno.voto, 7)
        self.assertEquals(resposta_retorno.descriçao, "otimo")
        self.assertEquals(resposta_retorno.comentario, "continue bem")
    

    def test_retorn(self):
        usuario_retorn = Usuario.objects.create(
            nome = "daniel",     
        )
        
        usuario_retorno = Usuario.objects.last()
        
        self.assertEquals(usuario_retorno.nome, "daniel")
        
        postagem_retorn = Postagem.objects.create(
            titulo = "vida"
        )
        
        postagem_retorn = Postagem.objects.last()
        
        self.assertEquals(postagem_retorn.titulo, "vida")
        