from django.db import models

class Alocacao(models.Model):
  id_projeto
  id_comp
  id_usuario
  id_alocacao
  inicio_alocacao
  fim_alocacao