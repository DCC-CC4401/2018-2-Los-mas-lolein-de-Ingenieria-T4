# Generated by Django 2.1.1 on 2018-11-15 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cevichecorp', '0003_auto_20181115_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnotienecoevaluacion',
            name='contestada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='coevaluacion',
            name='status',
            field=models.IntegerField(),
        ),
    ]