# Generated by Django 3.0.3 on 2020-07-03 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_remove_blogpost_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='author',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='body_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='comment_text',
            field=models.TextField(),
        ),
    ]