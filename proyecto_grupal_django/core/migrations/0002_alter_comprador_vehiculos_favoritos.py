# Generated by Django 4.2.5 on 2023-11-02 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprador',
            name='vehiculos_favoritos',
            field=models.ManyToManyField(blank=True, related_name='compradores_favoritos', to='core.vehiculo'),
        ),
    ]
