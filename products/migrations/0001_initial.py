# Generated by Django 4.0.3 on 2022-04-03 18:41

import cloudinary.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
                ('color_code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_short_name', models.CharField(max_length=25)),
                ('size_long_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('sku', models.CharField(default=uuid.uuid4, editable=False, max_length=8)),
                ('image', cloudinary.models.CloudinaryField(blank=True, default='No image provided', max_length=255, verbose_name='image')),
                ('price', models.FloatField(default=0.0, max_length=6)),
                ('categories', models.ManyToManyField(related_name='categories', to='products.category')),
                ('color', models.ManyToManyField(related_name='colors', to='products.color')),
                ('size', models.ManyToManyField(related_name='sizes', to='products.size')),
            ],
        ),
    ]
