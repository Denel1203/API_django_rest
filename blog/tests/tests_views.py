from django.test import TestCase
from django.urls import reverse


class UsuarioViewTestCase(TestCase):
    def test_usuario_views(self):
        response = self.client.get(reverse('Usuario_ViewSet'))
        self.assertEquals(response.status_code)