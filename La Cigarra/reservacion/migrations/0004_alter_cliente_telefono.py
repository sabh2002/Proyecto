# Generated by Django 4.2 on 2023-04-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservacion', '0003_alter_cliente_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]