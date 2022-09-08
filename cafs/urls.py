from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.views import ProjetoViewSet, ComputadorViewSet, AvisoViewSet, AlocacaoViewSet

router = DefaultRouter()
router.register(r"projetos", ProjetoViewSet)
router.register(r"computadores", ComputadorViewSet)
router.register(r"avisos", AvisoViewSet)
router.register(r"alocacoes", AlocacaoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]