# Generated by Django 3.0.3 on 2020-07-02 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200703_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='author',
        ),
        migrations.RemoveField(
            model_name='postcomment',
            name='author',
        ),
    ]
