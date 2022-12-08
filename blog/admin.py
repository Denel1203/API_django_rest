from django.contrib import admin

from .views import Postagem, Resposta, Usuario

admin.site.register(Usuario)
admin.site.register(Postagem)
admin.site.register(Resposta)


