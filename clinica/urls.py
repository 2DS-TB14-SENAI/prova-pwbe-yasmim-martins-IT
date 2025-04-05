from django.urls import path
from . import views

urlpatterns = [ path('medicos/', views.listar_medicos, name = 'listar_medicos'),
               path('consultas/nova/', views.criar_consultas, name = 'criar_consultas'),
                path ('consultas/<int:id>/', views.datalhes_consulta, name = 'detalhes_consultas'), 
                path ('', views.base , name = 'base' )
                ]
