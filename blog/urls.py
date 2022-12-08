from django.urls import include, path
from rest_framework import routers

from . import views

router=routers.DefaultRouter()
router.register('Usuario',views.Usuario_ViewSet)
router.register('Postagem',views.Postagem_ViewSet)
router.register('Resposta',views.Resposta_ViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('Respostar<int:id>/votar', views.Resposta_ViewSet.votar())
]
