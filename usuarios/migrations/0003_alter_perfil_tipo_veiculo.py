# Generated by Django 4.2 on 2023-04-27 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_perfil_options_perfil_cor_perfil_placa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='Tipo_veiculo',
            field=models.CharField(choices=[('Agregado', 'Agregado'), ('Icomon', 'Icomon'), ('Parceiro', 'Parceiro')], max_length=22),
        ),
    ]
