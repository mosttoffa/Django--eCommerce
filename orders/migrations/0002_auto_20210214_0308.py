# Generated by Django 3.1.5 on 2021-02-13 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_total',
            field=models.PositiveIntegerField(default=5.0),
        ),
    ]