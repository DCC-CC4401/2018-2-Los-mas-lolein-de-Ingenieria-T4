# Generated by Django 2.1.3 on 2018-11-19 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cevichecorp', '0005_auto_20181119_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuesta',
            name='id_pregunta',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='rut_desde',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='rut_objetivo',
        ),
        migrations.AddField(
            model_name='respuestasalumnos',
            name='nota',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Respuesta',
        ),
    ]