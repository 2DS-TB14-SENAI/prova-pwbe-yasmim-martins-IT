from django.shortcuts import render , get_object_or_404, redirect
from .models import Consulta , Medico
from rest_framework.response import Response
from rest_framework import status
from .form import ConsultaForms

def listar_medicos (request):
    medicos = Medico.objects.all().order_by('-nome')
    return render(request, 'clinica/listar_medicos.html', {'medicos': medicos})

def criar_consultas (request):
    if request.method == "POST":
        form = ConsultaForms(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('base')  
    else:
        form = ConsultaForms()  

    return render(request, 'clinica/form_consulta.html', {'form': form})  

def datalhes_consulta (request , pk):
    consulta = get_object_or_404(Consulta , pk = pk)
    if request.method== 'GET':
        return Response(consulta , status=status.HTTP_200_OK)
    else :
        Response ({'Erro' : 'Erro ao mostrar sua consulta'} , status= status.HTTP_204_NO_CONTENT)

def base (request) :
    return render(request, 'clinica/base.html')


# Create your views here.
