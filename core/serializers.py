from rest_framework.serializers import ModelSerializer

from core.models import Projeto, Computador, Aviso, Alocacao


class ProjetoSerializer(ModelSerializer):
    class Meta:
        model = Projeto
        fields = "__all__"


class ComputadorSerializer(ModelSerializer):
    class Meta:
        model = Computador
        fields = "__all__"


class AvisoSerializer(ModelSerializer):
    class Meta:
        model = Aviso
        fields = "__all__"


class AlocacaoSerializer(ModelSerializer):
    class Meta:
        model = Alocacao
        fields = "__all__"


class AlocacaoDetailSerializer(ModelSerializer):
    class Meta:
        model = Aviso
        fields = "__all__"
        depth = 1