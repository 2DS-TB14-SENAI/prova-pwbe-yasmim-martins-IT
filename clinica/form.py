from django import forms 
from .models import Consulta , Medico
from datetime import datetime as dt 

class ConsultaForms(forms.ModelForm) :
    class Meta :
        model = Consulta
        fields = '__all__'
    def clean_nome (self):
        nome = self.cleaned_data['nome']

        if len(nome) < 5 :
            raise forms.ValidationError('O nome deve ter no minimo 5 letras')
        return nome
    def clean_crm (self) :
        crm = self.cleaned_data['crm']

        if crm[2] != '/' :
            raise forms.ValidationError('O crm deve seguir o formato xx/xxx')
        return crm
class MedicoForms(forms.ModelForm) :
    class Meta :
        model = Medico
        fields = '__all__'