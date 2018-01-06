# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 00:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antecedente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enfermedad', models.CharField(help_text='Enfermedad que padece', max_length=32, verbose_name='Enfermedad')),
                ('familiar', models.CharField(default='Ninguno', max_length=100, verbose_name='¿Algún familiar también padece esta enfermedad?')),
                ('tratamiento', models.CharField(default='Ninguno', max_length=100, verbose_name='¿Le ha sido administrado algún tratamiento?')),
                ('medicamento_asignado', models.CharField(max_length=256, verbose_name='Medicamento asignado')),
            ],
            options={
                'verbose_name': 'Antecedente',
                'verbose_name_plural': 'Antecedentes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ConsultaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hora', models.TimeField(verbose_name='Hora de Consulta')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Peso')),
                ('talla', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Talla')),
                ('ta', models.CharField(help_text='Tension arterial ###/##', max_length=6, verbose_name='Tension arterial')),
                ('fc', models.DecimalField(decimal_places=2, help_text='Frecuencia cardiaca', max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Frecuencia cardiaca')),
                ('problema', models.CharField(help_text='Motivo de consulta', max_length=256, verbose_name='Historia del problema')),
                ('diagnostico', models.CharField(max_length=256, verbose_name='Diagnostico')),
                ('fecha_prox_control', models.DateField(verbose_name='Fecha proxima Consulta')),
                ('hora_prox_control', models.TimeField(blank=True, null=True, verbose_name='Hora')),
                ('precio_consulta', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Precio de la Consulta')),
            ],
            options={
                'verbose_name': 'Cita Medica',
                'verbose_name_plural': 'Citas Medicas',
                'ordering': ['fecha', 'hora'],
            },
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_apertura', models.DateField(auto_now_add=True, verbose_name='Fecha de apertura')),
            ],
            options={
                'verbose_name': 'Expediente',
                'verbose_name_plural': 'Expedientes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombres del paciente')),
                ('apellido', models.CharField(max_length=40, verbose_name='Apellidos del paciente')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='Sexo')),
                ('fecha_nacimiento', models.DateField(help_text='Formato: DD/MM/AAAA', verbose_name='Fecha de nacimiento')),
                ('telefono', models.CharField(help_text='Formato: XXXX-XXXX', max_length=9, unique=True, verbose_name='Número de teléfono')),
                ('direccion', models.CharField(help_text='Dirección de su residencia', max_length=80, verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'ordering': ['expediente'],
            },
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name='Fecha de prescripción')),
                ('hora', models.TimeField(verbose_name='Hora de prescripcion')),
                ('medicamento', models.CharField(max_length=256, verbose_name='Medicamento')),
                ('indicaciones', models.CharField(max_length=256, verbose_name='Indicaciones')),
                ('fk_receta_consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integral.ConsultaMedica')),
            ],
            options={
                'verbose_name': 'Receta',
                'verbose_name_plural': 'Recetas',
                'ordering': ['fecha'],
            },
        ),
        migrations.AddField(
            model_name='expediente',
            name='paciente',
            field=models.OneToOneField(help_text='Expediente asignado', on_delete=django.db.models.deletion.CASCADE, to='integral.Paciente'),
        ),
        migrations.AddField(
            model_name='consultamedica',
            name='fk_consulta_expediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integral.Expediente'),
        ),
        migrations.AddField(
            model_name='antecedente',
            name='fk_antecedente_expediente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='integral.Expediente'),
        ),
    ]
