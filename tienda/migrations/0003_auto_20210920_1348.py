# Generated by Django 3.2.5 on 2021-09-20 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_item_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='disponible',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
