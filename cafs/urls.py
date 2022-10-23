from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from core.views import ProjetoViewSet, ComputadorViewSet, AvisoViewSet, AlocacaoViewSet

router = DefaultRouter()
router.register(r"projetos", ProjetoViewSet)
router.register(r"computadores", ComputadorViewSet)
router.register(r"avisos", AvisoViewSet)
router.register(r"alocacoes", AlocacaoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
]
