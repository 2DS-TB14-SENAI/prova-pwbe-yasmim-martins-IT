from django.shortcuts import render 
from .models import Agendamento , Servico
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *

@api_view(['GET', 'POST'])
def listar_servicos(request) :
    if request.method == 'GET':
        servico = Servico.objects.all()

        serializer = Servico(servico , many = True)

        return Response(serializer.data , status= status.HTTP_200_OK)



# Create your views here.
