# Generated by Django 2.2.6 on 2019-11-04 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_auto_20191102_2353'),
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservas',
            name='servicio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='servicios.Servicios'),
        ),
    ]
