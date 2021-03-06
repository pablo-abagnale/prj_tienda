# Generated by Django 3.2.5 on 2021-09-13 16:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('marca', models.CharField(max_length=120)),
                ('categoria', models.CharField(max_length=120)),
                ('descripción', models.CharField(max_length=300, null=True)),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField()),
                ('disponible', models.BooleanField()),
                ('imagen', models.CharField(max_length=300, null=True)),
            ],
            options={
                'ordering': ['nombre', 'marca'],
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('nombre_cargo', models.CharField(max_length=70, primary_key=True, serialize=False, verbose_name='Cargo')),
                ('descripción', models.CharField(blank=True, max_length=150, null=True, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('num_categoria', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='Categoria')),
                ('beneficio', models.FloatField(default=0)),
                ('envio_gratis', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_alta', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de alta')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Cliente_categoria', to='tienda.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cp', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Localidades',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('num_doc', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Nº de documento')),
                ('apellido', models.CharField(max_length=70)),
                ('nombre', models.CharField(max_length=70, verbose_name='Nombre/s')),
                ('telefono', models.CharField(max_length=11)),
                ('mails', models.CharField(max_length=70)),
                ('fecha_nac', models.DateField(default=datetime.datetime.now, verbose_name='fecha de nacimiento')),
                ('localidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='persona_localidad', to='tienda.localidad')),
            ],
            options={
                'ordering': ['apellido', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=1)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('numero', models.CharField(max_length=70)),
                ('estado', models.BooleanField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Cliente_Moviento', to='tienda.cliente')),
            ],
            options={
                'ordering': ['tipo', 'fecha', 'cliente', 'estado'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Intem_Articulo', to='tienda.articulo')),
                ('movimiento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Item_Moviento', to='tienda.movimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legajo', models.IntegerField()),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Cargo_Empleado', to='tienda.cargo')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Empleado_persona', to='tienda.persona')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cliente_persona', to='tienda.persona'),
        ),
    ]
