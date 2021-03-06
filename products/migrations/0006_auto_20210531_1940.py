# Generated by Django 3.2 on 2021-05-31 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210531_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initial',
            name='name',
            field=models.CharField(help_text='Input here the name of your product, which you can later retrieve when noting transactions!', max_length=200),
        ),
        migrations.AlterField(
            model_name='initial',
            name='user',
            field=models.CharField(editable=False, max_length=100),
        ),
    ]
