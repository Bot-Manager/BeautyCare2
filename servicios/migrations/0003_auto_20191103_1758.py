# Generated by Django 2.2.6 on 2019-11-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_servicios_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterModelOptions(
            name='servicios',
            options={'verbose_name': 'servicio', 'verbose_name_plural': 'servicios'},
        ),
    ]
