"""
Rotas de URL do projeto SGO.
"""

from django.contrib import admin
from django.urls import path
from sgo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sobre/', views.about, name='about'),

    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/novo/', views.cliente_create, name='cliente_create'),
    path('clientes/editar/<int:pk>/', views.cliente_edit, name='cliente_edit'),
    path('clientes/excluir/<int:pk>/', views.cliente_delete, name='cliente_delete'),

    path('tecnicos/', views.tecnico_list, name='tecnico_list'),
    path('tecnicos/novo/', views.tecnico_create, name='tecnico_create'),
    path('tecnicos/editar/<int:pk>/', views.tecnico_edit, name='tecnico_edit'),
    path('tecnicos/excluir/<int:pk>/', views.tecnico_delete, name='tecnico_delete'),

    path('equipamentos/', views.equipamento_list, name='equipamento_list'),
    path('equipamentos/novo/', views.equipamento_create, name='equipamento_create'),
    path('equipamentos/editar/<int:pk>/', views.equipamento_edit, name='equipamento_edit'),
    path('equipamentos/excluir/<int:pk>/', views.equipamento_delete, name='equipamento_delete'),

    path('reparos/', views.reparo_list, name='reparo_list'),
    path('reparos/novo/', views.reparo_create, name='reparo_create'),
    path('reparos/editar/<int:pk>/', views.reparo_edit, name='reparo_edit'),
    path('reparos/excluir/<int:pk>/', views.reparo_delete, name='reparo_delete'),
    path('reparos/relatorio/<int:reparo_id>/', views.gerar_relatorio_pdf, name='gerar_relatorio_pdf'),
]
