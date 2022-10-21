from django.db import models

class Aviso(models.Model):
  id_aviso
  titulo_aviso = models.Charfield(max_length=255)
  desc_aviso = models.Charfield(max_length=100)
  data_pub_aviso = models.DateField(blank=True, null=True)
  id_usuario