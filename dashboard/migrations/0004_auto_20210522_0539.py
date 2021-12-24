# Generated by Django 3.2 on 2021-05-21 21:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_order_additionalexpenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='additionalExpenses',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
