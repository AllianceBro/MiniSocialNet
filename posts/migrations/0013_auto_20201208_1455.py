# Generated by Django 2.2.6 on 2020-12-08 11:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='Контентмейкер'),
        ),
    ]
