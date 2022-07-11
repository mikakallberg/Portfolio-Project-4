# Generated by Django 3.2.13 on 2022-07-11 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0011_auto_20220711_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='alt_tag',
            field=models.CharField(default='image related to post', max_length=100),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(default=94033831802592, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
