# Generated by Django 3.0.5 on 2020-10-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tye', '0002_auto_20201028_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
