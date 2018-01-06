from django import forms
from .models import Paciente, Expediente, Antecedente, ConsultaMedica, Receta, Antecedente


class nuevoPacienteForm(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = [
			'nombre',
			'apellido',
			'sexo',
			'fecha_nacimiento',
			'telefono',
			'direccion',
		]
		labels = {
			'nombre': 'Nombres',
			'apellido': 'Apellidoss',
			'sexo': 'Sexo',
			'fecha_nacimiento': 'Fecha de nacimiento',
			'telefono': 'Teléfono',
			'direccion': 'Dirección',
		}
		widget = {
			'nombre': forms.TextInput(),
			'apellido': forms.TextInput(),
			'sexo': forms.RadioSelect(),
			'fecha_nacimiento': forms.DateInput(),
			'telefono': forms.TextInput(),
			'direccion': forms.Textarea(),
		}


class nuevoExpedienteForm(forms.ModelForm):
	class Meta:
		model = Expediente
		fields = [
			'paciente',
		]
		labels = {
			'paciente': 'Paciente',
		}
		widget = {
			'paciente': forms.Select(),
		}



class ConsultaForm(forms.ModelForm):
	class Meta:
		model=ConsultaMedica

		fields = [
			'fecha',
			'hora',
			'peso',
			'talla',
			'ta',
			'fc',
			'problema',
			'diagnostico',
			'precio_consulta',
			'fk_consulta_expediente',
			'fecha_prox_control',
			'hora_prox_control',
		]

		labels= {
			'fecha':'Fecha de Consulta',
			'hora':' Hora de Consulta',
			'peso':'Peso',
			'talla':'Talla',
			'ta':'Tension Arterial',
			'fc':'Frecuencia Cardiaca',
			'problema':'Problema',
			'diagnostico':'Diagnostico',
			'precio_consulta':'Precio de Consulta',
			'fk_consulta_expediente':'Expediente Asignado',
			'fecha_prox_control':'Fecha de proximo control',
			'hora_prox_control':'Hora de proximo control',
		}

		widget = {
			'fecha':forms.DateField(),
			'hora':forms.TimeField(),
			'peso':forms.DecimalField(),
			'talla':forms.DecimalField(),
			'ta':forms.TextInput(),
			'fc':forms.DecimalField(),
			'problema':forms.TextInput(),
			'diagnostico':forms.TextInput(),
			'precio_consulta':forms.DecimalField(),
			'fk_consulta_expediente':forms.Select(),
			'fecha_prox_control':forms.DateField(),
			'hora_prox_control':forms.TimeField(),
		}

#RECETA FORM
class RecetaForm(forms.ModelForm):
	class Meta:
		model=Receta

		fields = [
			'fecha',
			'hora',
			'medicamento',
			'indicaciones',
		]

		labels= {
			'fecha':'Fecha de Consulta',
			'hora':' Hora de Consulta',
			'medicamento':'Medicamento',
			'indicaciones':'Indicaciones',
		}

		widget = {
			'fecha':forms.DateField(),
			'hora':forms.TimeField(),
			'medicamento':forms.TextInput(),
			'indicaciones':forms.TextInput(),
		}

#Antecedente_FORM
class AntecedenteForm(forms.ModelForm):
	class Meta:
		model=Antecedente

		fields = [
			'enfermedad',
			'familiar',
			'tratamiento',
			'medicamento_asignado',
		]

		labels= {
			'enfermedad':'Enfermedades que ha padecido',
			'familiar':' Familiar que padece esta enfermedad',
			'tratamiento':'Tratamiento recomendado',
			'medicamento_asignado':'Medicina aplicada',
		}

		widget = {
			'enfermedad':forms.TextInput(),
			'familiar':forms.TextInput(),
			'tratamiento':forms.TextInput(),
			'medicamento_asignado':forms.TextInput(),
		}

