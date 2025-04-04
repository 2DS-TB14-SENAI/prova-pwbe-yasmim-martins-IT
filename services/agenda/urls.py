from django.urls import path
from . import views

urlpatterns = [ path('GET/api/servicos/', views.listar_servicos),
                ]