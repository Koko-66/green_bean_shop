# Generated by Django 4.0.3 on 2022-04-08 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='category',
        ),
    ]
