# Generated by Django 2.0.3 on 2018-06-16 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unAventonApp', '0006_auto_20180613_0013'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoViaje',
        ),
        migrations.AlterField(
            model_name='conversacionpublica',
            name='fechaHoraRespuesta',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]