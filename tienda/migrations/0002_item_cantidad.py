# Generated by Django 3.2.5 on 2021-09-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]
