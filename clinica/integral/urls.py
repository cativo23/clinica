from django.conf.urls import include, url
from .views import PacienteList, PacienteDetail, PacienteDelete,Consulta_Medica, ConsultaDelete, detalleConsulta, nuevaConsulta, Receta_Medica, detalleRecetas, detalleReceta, nuevaReceta, antecedentes, detalleAntecedente, nuevoAntecedente
from .views import index, nuevoPaciente, expediente


urlpatterns = [
	url(r'^$', index, name = 'index'),
	url(r'^pacientes$', PacienteList.as_view(), name='listarPaciente'),
	#url(r'^listarAntecedentes/(?P<expedienteId>\d+)$', AntecedenteList, name='listarAntecedentes'),
	url(r'^detallePaciente/(?P<pk>\d+)$', PacienteDetail.as_view(), name='detallePaciente'),
	url(r'^eliminarPaciente/(?P<pk>\d+)$', PacienteDelete.as_view(), name='eliminarPaciente'),
	# url(r'^eliminarConsulta/(?P<pk>\d+)$', ConsultaDelete.as_view(), name='eliminarConsulta'),
	url(r'^nuevoPaciente/$', nuevoPaciente, name='nuevoPaciente'),
	url(r'^expediente/$', expediente, name = 'expedientes'),
	url(r'^ConsultasMedica/(?P<expedienteId>\d+)/$',Consulta_Medica, name='ConsultaMedica'),
	url(r'^detalleConsulta/(?P<consultaId>\d+)/(?P<expedienteId>\d+)$', detalleConsulta, name='detalle_Consulta'),
	url(r'^nuevaConsulta/(?P<expedienteId>\d+)$', nuevaConsulta, name='nuevaConsulta'),
	url(r'^RecetasMedica/(?P<consultaId>\d+)/$',Receta_Medica, name='RecetaMedica'),
	url(r'^detalleReceta/(?P<recetaId>\d+)/(?P<consultaId>\d+)$', detalleReceta, name='detalle_Consulta'),
	url(r'^detalleRecetas/(?P<consultaId>\d+)$', detalleRecetas, name='detalle_Consultas'),
	url(r'^nuevaReceta/(?P<consultaId>\d+)$', nuevaReceta, name='nuevaReceta'),
	url(r'^antecedentes/(?P<expedienteId>\d+)/$',antecedentes, name='antecedentes'),
	url(r'^detalleAntecedente/(?P<antecedenteId>\d+)/(?P<expedienteId>\d+)$', detalleAntecedente, name='detalle_antecedente'),
	url(r'^nuevoAntecedente/(?P<expedienteId>\d+)$', nuevoAntecedente, name='nuevoAntecedente'),
]
