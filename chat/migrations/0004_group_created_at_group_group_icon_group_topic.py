# Generated by Django 5.0.1 on 2024-04-19 09:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_chat_group_alter_chat_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='group',
            name='group_icon',
            field=models.ImageField(blank=True, null=True, upload_to='group_icons/'),
        ),
        migrations.AddField(
            model_name='group',
            name='topic',
            field=models.TextField(blank=True),
        ),
    ]
