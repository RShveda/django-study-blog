# Generated by Django 3.0.3 on 2020-07-03 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200703_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='created_time',
        ),
    ]
