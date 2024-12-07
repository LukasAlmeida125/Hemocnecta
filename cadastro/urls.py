from django.urls import path
from . import views

urlpatterns=[
    path('cadastro/',views.paginaCadastro,name='cadastro'),
    path('login/',views.paginaLogin, name='login'),
    path('', views.inicial, name='inicial'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('historico/', views.historico, name='historico'),
    path('tabela/', views.tabela, name='tabela'),
    path('conf/', views.conf, name='conf'),
    path('notificacao/', views.notificacao, name='notificacao')
]