# Generated by Django 2.2.6 on 2019-11-03 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0004_auto_20191103_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicios',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='servicios.Categoria'),
        ),
    ]
