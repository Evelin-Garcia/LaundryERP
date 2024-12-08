# Generated by Django 4.2.16 on 2024-12-05 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenDeServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estatus', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Completada', 'Completada')], max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.cliente')),
                ('empleado', models.ForeignKey(limit_choices_to={'rol': 'empleado'}, on_delete=django.db.models.deletion.CASCADE, to='usuarios.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Prenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_prenda', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenPrenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenes.ordendeservicio')),
                ('prenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenes.prenda')),
            ],
        ),
        migrations.AddField(
            model_name='ordendeservicio',
            name='prendas',
            field=models.ManyToManyField(through='ordenes.OrdenPrenda', to='ordenes.prenda'),
        ),
    ]
