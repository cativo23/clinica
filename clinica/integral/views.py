from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from .models import Paciente, Expediente, Antecedente, ConsultaMedica, Receta, Antecedente
from .forms import nuevoPacienteForm, nuevoExpedienteForm, ConsultaForm, RecetaForm, AntecedenteForm
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
import json
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

@login_required
def index(request):
	return render(request, 'integral/index.html',{})


@login_required
def nuevoPaciente(request):
	pacientes = Paciente.objects.all()
	paginator = Paginator(pacientes,15)
	page = request.GET.get('page')
	try:
		pacientes = paginator.page(page)
	except PageNotAnInteger:
		pacientes = paginator.page(1)
	except EmptyPage:
		pacientes = paginator.page(paginator.num_pages)
	if request.method == 'POST':
		form = nuevoPacienteForm(request.POST)
		if form.is_valid():
			form.save()
			ultimoPaciente = Paciente.objects.first()
			Expediente.objects.create(paciente = ultimoPaciente)
			messages.success(request, 'Paciente correctamente guardado!')
			return redirect('integral:listarPaciente')
		else:
			data = json.dumps([v for k , v in form.errors.items()]+[' ¡Error!'])
			return HttpResponse(data, content_type='application/json')
	else:
		form = nuevoPacienteForm()
	return render(request, 'integral/nuevoPaciente.html', {'form': form,'pacientes':pacientes})


@login_required
def expediente(request):
	expedientes = Expediente.objects.all()
	paginator = Paginator(expedientes,15)
	page = request.GET.get('page')
	try:
		expedientes = paginator.page(page)
	except PageNotAnInteger:
		expedientes = paginator.page(1)
	except EmptyPage:
		expedientes = paginator.page(paginator.num_pages)
	if request.method == 'POST':
		form = nuevoExpedienteForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Correctamente guardado!')
			return HttpResponse("GUARDADO!")
		else:
		    data = json.dumps([v for k , v in form.errors.items()]+[' ¡Error!'])
		return HttpResponse(data, content_type='application/json')
	else:
		form = nuevoExpedienteForm()
	return render(request, 'integral/expediente/expediente.html',{'form':form,'expedientes':expedientes})

#def AntecedenteList(request,expedienteId):
#	antecedentes = Antecedente.objects.filter(fk_antecedente_expediente=expedienteId)
#	return render(request, 'integral/antecedente_list.html',{'antecedentes':antecedentes})

class PacienteList(LoginRequiredMixin, ListView):
	model = Paciente


class PacienteDetail(LoginRequiredMixin, DetailView):
	model = Paciente


class PacienteDelete(LoginRequiredMixin, DeleteView):
	model = Paciente
	success_message = "Paciente eliminado correctamente"
	success_url = reverse_lazy('integral:listarPaciente')

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(PacienteDelete, self).delete(request, *args, **kwargs)


class ConsultaDelete(LoginRequiredMixin, DeleteView):
	model = ConsultaMedica
	success_message = "Consulta eliminada correctamente"

	def get_success_url(self):
		expediente = self.object.fk_consulta_expediente
		return reverse_lazy( 'integral:eliminarConsulta', kwargs={'expedienteId': expediente.id})

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(ConsultaDelete, self).delete(request, *args, **kwargs)

# class AntecedenteList(ListView):
# model = Antecedente
@login_required
def Consulta_Medica(request,expedienteId):
	consulta = ConsultaMedica.objects.filter(fk_consulta_expediente=expedienteId)
	expediente= expedienteId
	return render(request, 'integral/Consulta_Expediente.html',{'consultaMedica':consulta,'expedienteId':expediente})


@login_required
def detalleConsulta(request,consultaId,expedienteId):
	consulta = ConsultaMedica.objects.filter(id=consultaId)
	datos = Paciente.objects.filter(id=expedienteId)
	nombre = Paciente.objects.get(id=expedienteId)
	expediente=expedienteId
	return render(request, 'integral/consultamedica_detail.html',{'conId':consultaId, 'consultaMedica':consulta,'expedienteId':expediente,'paciente':datos, 'nombre':nombre})


@login_required
def nuevaConsulta(request,expedienteId):
	expediente= expedienteId
	datos = Paciente.objects.get(id=expedienteId)
	if request.method == 'POST':
		ConsultaMedica.objects.create(
			fecha=request.POST['fechaActual'],
			hora=request.POST['horaActual'],
			peso=request.POST['PesoPaciente'],
			talla=request.POST['TallaPaciente'],
			ta=request.POST['TensionArterial'],
			fc=request.POST['FrecuenciaCardiaca'],
			problema=request.POST['ProblemaEnfermedad'],
			diagnostico=request.POST['DiagnosticoEnfermedad'],
			fecha_prox_control=request.POST['fechaProxActual'],
			hora_prox_control =request.POST['horaProxActual'],
			precio_consulta=request.POST['PrecioConsulta'],
			fk_consulta_expediente=Expediente.objects.get(id=request.POST['expediente'])
		)
		messages.success(request, 'Correctamente guardado!')
		return HttpResponse('Datos Almacenados Correctamente')
	return render(request,'integral/nuevaConsulta.html',{'expedienteId':expediente, 'paciente':datos})

# RECETAS VIEWS
@login_required
def Receta_Medica(request,consultaId):
	receta = Receta.objects.filter(fk_receta_consulta=consultaId)
	consulta= ConsultaMedica.objects.get(id=consultaId)
	return render(request, 'integral/Receta_Consulta.html',{'recetaMedica':receta,'consulta':consulta})


@login_required
def detalleReceta(request,recetaId,consultaId):
	receta = Receta.objects.filter(id= recetaId)
	datos = ConsultaMedica.objects.get(id=consultaId)
	expediente = datos.fk_consulta_expediente
	print(expediente.id)
	consulta=consultaId
	return render(request, 'integral/recetamedica_detail.html',{'receta':receta,'consultaId':consulta,'consulta':datos, 'expediente':expediente})


def detalleRecetas(request,consultaId):
	receta = Receta.objects.filter(fk_receta_consulta=consultaId)
	datos = ConsultaMedica.objects.get(id=consultaId)
	expediente = datos.fk_consulta_expediente
	print(expediente.id)
	consulta=consultaId
	return render(request, 'integral/recetamedica_detail.html',{'receta':receta,'consultaId':consulta,'consulta':datos, 'expediente':expediente})


@login_required
def nuevaReceta(request,consultaId):
	consulta = consultaId
	datos = ConsultaMedica.objects.get(id=consultaId)
	print(consultaId)
	if request.method == 'POST':
		Receta.objects.create(
			fk_receta_consulta=ConsultaMedica.objects.get(id=consultaId),
			fecha=request.POST['fechaActual'],
			hora=request.POST['horaActual'],
			medicamento=request.POST['MedicamentoPaciente'],
			indicaciones=request.POST['IndicacionesPaciente'],
		)
		messages.success(request, 'Correctamente guardado!')
		return HttpResponse('Datos Almacenados Correctamente')
	return render(request,'integral/nuevaReceta.html',{'consultaId':consulta, 'consulta':datos})


#Antecedente_views
@login_required
def antecedentes(request,expedienteId):
	antecedente = Antecedente.objects.filter(fk_antecedente_expediente=expedienteId)
	expediente= expedienteId
	datos = Expediente.objects.get(id=expedienteId)
	return render(request, 'integral/Antecedente_Expediente.html',{'antecedentes':antecedente,'expedienteId':expediente, 'expe':datos})


@login_required
def detalleAntecedente(request,antecedenteId,expedienteId):
	antecedente = Antecedente.objects.get(id=antecedenteId)
	datos = Expediente.objects.get(id=expedienteId)
	expediente=expedienteId
	return render(request, 'integral/antecedente_detail.html',{'antecedente':antecedente,'expedienteId':expediente,'paciente':datos})


@login_required
def nuevoAntecedente(request,expedienteId):
	expediente = expedienteId
	if request.method == 'POST':
		Antecedente.objects.create(
			fk_antecedente_expediente=Expediente.objects.get(id=expedienteId),
			enfermedad=request.POST['enfermedad'],
			familiar=request.POST['familiar'],
			tratamiento=request.POST['tratamiento'],
			medicamento_asignado=request.POST['medicamento_asignado'],
		)
		messages.success(request, 'Correctamente guardado!')
		return HttpResponse('Datos Almacenados Correctamente')
	return render(request,'integral/nuevoAntecedente.html',{'expedienteId':expediente})
