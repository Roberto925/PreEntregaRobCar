# Generated by Django 4.1.6 on 2023-03-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_paciente_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='turnos',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='turnos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
