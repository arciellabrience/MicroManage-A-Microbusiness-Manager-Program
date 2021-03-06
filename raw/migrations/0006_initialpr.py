# Generated by Django 3.2 on 2021-05-25 18:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw', '0005_initial_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitialPR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(editable=False, max_length=100)),
                ('product', models.CharField(editable=False, max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('materialType', models.CharField(max_length=200)),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('unitType', models.CharField(max_length=200)),
                ('totalCost', models.DecimalField(decimal_places=2, max_digits=100)),
            ],
        ),
    ]
