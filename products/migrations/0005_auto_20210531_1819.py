# Generated by Django 3.2 on 2021-05-31 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_initial_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initial',
            name='itemType',
            field=models.CharField(help_text='Add here the type of item that you are selling so you have an easy reference when checking your database.', max_length=200),
        ),
        migrations.AlterField(
            model_name='initial',
            name='sellPrice',
            field=models.DecimalField(decimal_places=2, help_text='Put here the selling price of this type of product which will be the basis of tracking your income later on!', max_digits=100),
        ),
        migrations.AlterField(
            model_name='initial',
            name='user',
            field=models.CharField(editable=False, help_text='Input here the name of your product, which you can later retrieve when noting transactions!', max_length=100),
        ),
    ]
