# Generated by Django 4.0.3 on 2022-04-05 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_product_ype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_ype',
            new_name='product_type',
        ),
    ]