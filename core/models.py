from django.db import models
from django.contrib.auth.models import User


class Projeto(models.Model):
    titulo = models.CharField(max_length=128)
    descricao = models.CharField(max_length=255)
    data_inicial = models.DateField()
    data_final = models.DateField()
    usuario = models.ManyToManyField(User, related_name="projetos")

    def __str__(self):
        return f"{self.titulo} ({self.descricao})"


class Computador(models.Model):
    numero = models.CharField(max_length=4)
    linha = models.CharField(max_length=7)
    coluna = models.CharField(max_length=7)

    class Meta:
        verbose_name_plural = "Computadores"

    def __str__(self):
        return self.numero


class Aviso(models.Model):
    data_publicacao = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=128)
    descricao = models.CharField(max_length=255)
    publicado_por = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="avisos"
    )

    def __str__(self):
        return self.titulo


class Alocacao(models.Model):
    data_alocacao = models.DateTimeField(auto_now_add=True)
    projeto = models.ForeignKey(
        Projeto, on_delete=models.CASCADE, related_name="alocacoes"
    )
    computador = models.ForeignKey(
        Computador, on_delete=models.CASCADE, related_name="alocacoes"
    )
    alocado_por = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="alocacoes"
    )
    alocacao_inicio = models.DateTimeField()
    alocacao_final = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Alocacoes"

    def __str__(self):
        return self.data_alocacao