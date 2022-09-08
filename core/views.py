from rest_framework.viewsets import ModelViewSet


from core.models import Projeto, Computador, Aviso, Alocacao
from core.serializers import (
    ProjetoSerializer,
    ComputadorSerializer,
    AvisoSerializer,
    AlocacaoSerializer,
    AlocacaoDetailSerializer,
)


class ProjetoViewSet(ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer


class ComputadorViewSet(ModelViewSet):
    queryset = Computador.objects.all()
    serializer_class = ComputadorSerializer


class AvisoViewSet(ModelViewSet):
    queryset = Aviso.objects.all()
    serializer_class = AvisoSerializer


class AlocacaoViewSet(ModelViewSet):
    queryset = Alocacao.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return AlocacaoDetailSerializer
        return AlocacaoSerializer