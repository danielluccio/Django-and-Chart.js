# Generated by Django 5.0.7 on 2024-07-22 19:08

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Venda",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total", models.FloatField()),
                (
                    "data",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 7, 22, 16, 8, 42, 265034)
                    ),
                ),
                (
                    "nome_vendedor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="App.funcionario",
                    ),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="App.produto"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Vendas",
        ),
    ]
