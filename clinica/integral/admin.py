from django.contrib import admin
from .models import Paciente, Expediente, Antecedente, ConsultaMedica, Receta

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Expediente)
admin.site.register(Antecedente)
admin.site.register(ConsultaMedica)
admin.site.register(Receta)

