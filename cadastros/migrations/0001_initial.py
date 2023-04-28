# Generated by Django 4.2 on 2023-04-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=20)),
                ('Area', models.CharField(max_length=20, verbose_name='Área')),
                ('Funcao', models.CharField(max_length=20, verbose_name='Função')),
                ('Numero', models.CharField(max_length=20, verbose_name='Número')),
                ('Base', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Contatos',
                'verbose_name_plural': 'Contatos',
            },
        ),
        migrations.CreateModel(
            name='Obras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Não iniciado', 'Não iniciado'), ('Iniciado', 'Iniciado'), ('Pendênciado', 'Pendênciado')], max_length=12)),
                ('DC', models.CharField(max_length=50)),
                ('Colaborador_1', models.CharField(max_length=50, verbose_name='Colaborador 1°')),
                ('Colaborador_2', models.CharField(max_length=50, verbose_name='Colaborador 2°')),
                ('Fotos', models.FileField(default=None, null=True, upload_to='uploads')),
                ('Obs', models.TextField(max_length=500, verbose_name='Observação')),
                ('status_final', models.CharField(choices=[('Não iniciado', 'Não iniciado'), ('Pendênciado', 'Pendênciado'), ('Em andamento', 'Em andamento'), ('Finalizado', 'Finalizado')], max_length=12)),
                ('Data', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data da Criação')),
            ],
            options={
                'verbose_name': 'Cadastro De Obras',
                'verbose_name_plural': 'Cadastros De Obras',
            },
        ),
    ]
