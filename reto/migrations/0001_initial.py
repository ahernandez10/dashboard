# Generated by Django 4.1.1 on 2022-09-21 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('edad', models.CharField(max_length=200)),
                ('peso', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequenciaCardiaca', models.CharField(max_length=65, verbose_name='Frequencia Cardiaca(Heart Rate)')),
                ('saturacionOxigeno', models.CharField(max_length=65, verbose_name='Saturacion De Oxigeno en Sangre')),
                ('nivelEstres', models.CharField(choices=[('a', 'Alto'), ('b', 'Bajo'), ('n', 'Normal')], max_length=1, verbose_name='Nivel De Estres')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reto.person')),
            ],
        ),
    ]
