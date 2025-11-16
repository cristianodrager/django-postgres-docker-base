from django.contrib import admin
from .models import Turma, Disciplina, Presenca, RegistroSaida, ConfirmacaoSaida

# Register your models here.
admin.site.register(Turma)
admin.site.register(Disciplina)
admin.site.register(Presenca)
admin.site.register(RegistroSaida)
admin.site.register(ConfirmacaoSaida)
