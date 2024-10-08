# Generated by Django 5.0.3 on 2024-07-03 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0009_conexion'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySQLConnection',
            fields=[
                ('id_conexion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_conexion', models.CharField(max_length=255)),
                ('usuario_conexion', models.CharField(max_length=255)),
                ('password_conexion', models.CharField(max_length=255)),
                ('host_conexion', models.CharField(max_length=255)),
                ('puerto_conexion', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Conexion',
        ),
    ]
