# Generated by Django 4.1.1 on 2022-09-08 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Computador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=3)),
                ('linha', models.CharField(max_length=7)),
                ('coluna', models.CharField(max_length=7)),
            ],
            options={
                'verbose_name_plural': 'Computadores',
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=128)),
                ('descricao', models.CharField(max_length=255)),
                ('data_inicial', models.DateField()),
                ('data_final', models.DateField()),
                ('usuario', models.ManyToManyField(related_name='projetos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Aviso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=128)),
                ('descricao', models.CharField(max_length=255)),
                ('publicado_por', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='avisos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Alocacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_alocacao', models.DateTimeField(auto_now_add=True)),
                ('alocacao_inicio', models.DateTimeField()),
                ('alocacao_final', models.DateTimeField()),
                ('alocado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alocacoes', to=settings.AUTH_USER_MODEL)),
                ('computador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alocacoes', to='core.computador')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alocacoes', to='core.projeto')),
            ],
            options={
                'verbose_name_plural': 'Alocacoes',
            },
        ),
    ]