# Generated by Django 3.0.5 on 2020-09-25 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tye', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='instructor_pics'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='sessionName',
            field=models.CharField(max_length=50),
        ),
    ]
