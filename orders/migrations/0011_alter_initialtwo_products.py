# Generated by Django 3.2 on 2021-05-31 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20210530_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialtwo',
            name='products',
            field=models.CharField(choices=[('hi', 'hi'), ('bye', 'bye')], default=6, max_length=20),
            preserve_default=False,
        ),
    ]
