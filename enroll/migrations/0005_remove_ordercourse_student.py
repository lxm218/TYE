# Generated by Django 3.0.5 on 2020-10-28 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0004_ordercourse_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordercourse',
            name='student',
        ),
    ]
