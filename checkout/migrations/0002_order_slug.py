# Generated by Django 4.0.3 on 2022-04-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='slug',
            field=models.SlugField(default=980808080, max_length=32, unique=True),
            preserve_default=False,
        ),
    ]
