# Generated by Django 4.0.3 on 2022-05-17 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_rating_product_alter_rating_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='comment',
            field=models.TextField(default='no comment', max_length=1500),
            preserve_default=False,
        ),
    ]
