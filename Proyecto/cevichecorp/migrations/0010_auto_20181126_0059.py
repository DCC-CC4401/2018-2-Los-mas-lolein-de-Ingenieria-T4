# Generated by Django 2.1.1 on 2018-11-26 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cevichecorp', '0009_auto_20181126_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perteneceacurso',
            name='rol',
            field=models.CharField(choices=[('alumno', 'Estudiante'), ('profesor', 'Profesor'), ('auxiliar', 'Profesor auxiliar'), ('ayudante', 'Ayudante')], max_length=20),
        ),
    ]
