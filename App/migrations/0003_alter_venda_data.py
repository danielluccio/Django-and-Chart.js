# Generated by Django 5.0.7 on 2024-07-22 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0002_venda_delete_vendas"),
    ]

    operations = [
        migrations.AlterField(
            model_name="venda",
            name="data",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 7, 22, 16, 10, 47, 744679)
            ),
        ),
    ]
