# Generated by Django 5.1.4 on 2025-02-03 14:21

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0013_alter_customuser_cpf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="categoria",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="users.categoria",
                verbose_name="Categoria",
            ),
        ),
        migrations.AlterField(
            model_name="produto",
            name="fornecedor",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="users.fornecedor",
                verbose_name="Fornecedor",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="produto",
            name="quantity",
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinLengthValidator(1),
                    django.core.validators.MaxLengthValidator(10),
                ],
                verbose_name="quantity",
            ),
        ),
    ]
