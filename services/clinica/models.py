from django.db import models
from django.core.validators import MaxLengthValidator , MinLengthValidator


class Medico(models.Model):
    nome = models.CharField(max_length=200, validators= [MinLengthValidator(5)])
    escolhas = [
        ("CAR","Cardiologista"),
        ("ORT" , "Ortopedista"),
        ('GO', 'Ginecologista Obstreta')
    ]
    especialidade = models.CharField(max_length=20 , choices= escolhas)
    crm = models.CharField( max_length= 7 ,unique= True )
    email = models.EmailField(blank= True)
    
    def __str__(self):
        return self.nome
# Create your models here.

class Consulta(models.Model):
    paciente = models.CharField(max_length= 200)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    escolhas = [
        ('AGENDADO' , 'agendado'),
        ('REALIZADO' , 'realizado'),
        ('CANCELADO' , 'cancelado')
    ]
    status = models.CharField(max_length=20 , choices= escolhas)

    def __str__(self):
        return self.paciente