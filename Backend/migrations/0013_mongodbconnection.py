# Generated by Django 5.0.3 on 2024-07-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0012_postgresqlconnection'),
    ]

    operations = [
        migrations.CreateModel(
            name='MongoDbConnection',
            fields=[
                ('id_conexion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_conexion', models.CharField(max_length=255)),
                ('usuario_conexion', models.CharField(max_length=255)),
                ('password_conexion', models.CharField(max_length=255)),
                ('host_conexion', models.CharField(max_length=255)),
                ('puerto_conexion', models.IntegerField()),
            ],
            options={
                'db_table': 'mongodb',
            },
        ),
    ]
