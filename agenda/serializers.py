from .models import *
from rest_framework import serializers

class ServicosSerializer (serializers.Serializer) :
    class Meta :
        model = Servico
        fields = "__all__"

class AgendamentoSerializer (serializers.Serializer) :
    class Meta :
        model = Agendamento
        fields = "__all__"

        