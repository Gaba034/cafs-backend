from django.db import models

class Aviso(models.Model):
  id_aviso
  titulo_aviso
  desc_aviso
  data_pub_aviso
  id_usuario