# Generated by Django 3.2 on 2021-05-23 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210510_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='initial',
            name='user',
            field=models.CharField(default=12345, editable=False, max_length=100),
            preserve_default=False,
        ),
    ]
