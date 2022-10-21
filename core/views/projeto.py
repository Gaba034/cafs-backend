from django.db import models

class Projeto(Model.Models):
  projeto = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="projetos"
    )
  titulo_projeto = models.Charfield(max_length=255)
  desc_projeto = models.Charfield(max_length=100)
  data_inicial
  data_final
  usuario = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="projetos"
    )