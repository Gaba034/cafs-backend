from django.contrib import admin

from core.models import Projeto, Computador, Aviso, Alocacao

admin.site.register(Projeto)
admin.site.register(Computador)
admin.site.register(Aviso)
admin.site.register(Alocacao)