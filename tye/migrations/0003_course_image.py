# Generated by Django 3.0.5 on 2020-09-25 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tye', '0002_auto_20200925_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='course_pics'),
        ),
    ]