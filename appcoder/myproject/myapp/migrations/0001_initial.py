# Generated by Django 4.1.6 on 2023-03-08 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('especialidad', models.CharField(max_length=30)),
                ('turnosDisp', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('obraSocial', models.CharField(max_length=30)),
                ('nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomPaciente', models.CharField(max_length=30)),
                ('fecha', models.DateTimeField()),
                ('especial', models.CharField(max_length=30)),
            ],
        ),
    ]
