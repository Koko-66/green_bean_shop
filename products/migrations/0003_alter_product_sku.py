# Generated by Django 4.0.3 on 2022-04-03 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_size_long_name_size_size_long_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
