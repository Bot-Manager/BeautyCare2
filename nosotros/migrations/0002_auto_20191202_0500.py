# Generated by Django 2.2.6 on 2019-12-02 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nosotros', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AcercaDe',
            new_name='Nosotros',
        ),
        migrations.AlterModelOptions(
            name='nosotros',
            options={'verbose_name': 'nosotros', 'verbose_name_plural': 'nosotros'},
        ),
        migrations.AlterModelOptions(
            name='pasion',
            options={'verbose_name': 'pasion', 'verbose_name_plural': 'pasion'},
        ),
        migrations.AlterModelOptions(
            name='profesional',
            options={'verbose_name': 'profesional', 'verbose_name_plural': 'profesional'},
        ),
    ]