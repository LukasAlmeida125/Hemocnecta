from django.contrib import admin
from .models import Cadastrar, Agendamento

# Register your models here.

class CadastrarAdmin(admin.ModelAdmin):
    list_display =('nome', 'cpf','tipo_sang')
    list_per_page = int = 15
    model = Cadastrar

class AgendamentoAdmin(admin.ModelAdmin):
    list_display =('nomeA', 'cpfA', 'agendamento_data', 'agendamento_hora')
    list_per_page = int = 15
    model = Agendamento


admin.site.register(Cadastrar, CadastrarAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)


