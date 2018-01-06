from django.db import models
from django.core.validators import MinValueValidator

SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)


class Paciente(models.Model):
    nombre = models.CharField('Nombres del paciente', max_length=40, blank=False, null=False)
    apellido = models.CharField('Apellidos del paciente', max_length=40, blank=False, null=False)
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', help_text='Formato: DD/MM/AAAA', blank=False, null=False)
    telefono = models.CharField('Número de teléfono', max_length=9, help_text='Formato: XXXX-XXXX', blank=False, null=False, unique=True)
    direccion = models.CharField('Dirección', max_length=80, help_text='Dirección de su residencia', blank=False, null=False)

    def __str__(self):
        return '{} {}'.format(self.apellido, self.nombre)

    class Meta:
        ordering = ['expediente']
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


class Expediente(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.OneToOneField(Paciente, null=False, help_text='Expediente asignado')
    fecha_apertura = models.DateField('Fecha de apertura', auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format('Expediente de', self.paciente)

    class Meta:
        ordering = ["id"]
        verbose_name = 'Expediente'
        verbose_name_plural = 'Expedientes'


class Antecedente(models.Model):
    fk_antecedente_expediente = models.ForeignKey(Expediente, null=True, blank=True)
    enfermedad = models.CharField('Enfermedad', max_length=32, blank=False, null=False, help_text='Enfermedad que padece')
    familiar = models.CharField('¿Algún familiar también padece esta enfermedad?',max_length=100, default='Ninguno')
    tratamiento = models.CharField('¿Le ha sido administrado algún tratamiento?',max_length=100, default='Ninguno')
    medicamento_asignado = models.CharField('Medicamento asignado', max_length=256, blank=False, null=False)

    def __str__(self):
        return self.enfermedad

    class Meta:
        ordering = ["id"]
        verbose_name = 'Antecedente'
        verbose_name_plural = 'Antecedentes'


class ConsultaMedica(models.Model):
    fk_consulta_expediente = models.ForeignKey(Expediente, null=False, blank=False)
    fecha = models.DateField('Fecha', auto_now_add=False)
    hora = models.TimeField('Hora de Consulta', blank=False, null=False)
    peso = models.DecimalField('Peso', max_digits=5, decimal_places=2, blank=False, null=False, validators=[MinValueValidator(0)])
    talla = models.DecimalField('Talla', max_digits=5, decimal_places=2, blank=False, null=False, validators=[MinValueValidator(0)])
    ta = models.CharField('Tension arterial', max_length=6, blank=False, null=False, help_text='Tension arterial ###/##')
    fc = models.DecimalField('Frecuencia cardiaca', max_digits=5, decimal_places=2, blank=False, null=False, help_text='Frecuencia cardiaca', validators=[MinValueValidator(0)])
    problema = models.CharField('Historia del problema', max_length=256, blank=False, null=False, help_text='Motivo de consulta')
    diagnostico = models.CharField('Diagnostico', max_length=256, blank=False, null=False)
    fecha_prox_control = models.DateField('Fecha proxima Consulta', auto_now_add=False)
    hora_prox_control = models.TimeField('Hora', blank=True, null=True)
    precio_consulta = models.DecimalField('Precio de la Consulta', max_digits=5, decimal_places=2, blank=False, null=False, validators=[MinValueValidator(0)])

    def __str__(self):
        return '{}: {}'.format('Consulta del expediente', self.fk_consulta_expediente)

    def get_edad(self):
        diff = (self.fecha - self.fk_consulta_expediente.paciente.fecha_nacimiento).days
        edad = str(int(diff / 365))
        cantidad_tiempo = 'anios'
        if edad == '0':
            edad = str(int(diff / 12))
            cantidad_tiempo = 'meses'
        return '{} {}'.format(self.edad, self.cantidad_tiempo)

    class Meta:
        ordering = ["fecha", "hora"]
        verbose_name = 'Cita Medica'
        verbose_name_plural = 'Citas Medicas'


class Receta(models.Model):
    fk_receta_consulta = models.ForeignKey(ConsultaMedica, null=False, blank=False)
    fecha = models.DateTimeField('Fecha de prescripción', auto_now_add=False)
    hora = models.TimeField('Hora de prescripcion', blank= False, null= False)
    medicamento = models.CharField('Medicamento', max_length=256, blank=False, null=False)
    indicaciones = models.CharField('Indicaciones', max_length=256, blank=False, null=False)

    def __str__(self):
        return '{} {} {}'.format(self.fecha, self.hora, self.fk_receta_consulta)

    class Meta:
        ordering = ['fecha']
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
