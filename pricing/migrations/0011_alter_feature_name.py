# Generated by Django 5.0.1 on 2024-04-18 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0010_remove_plan_feature_feature_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='name',
            field=models.CharField(help_text='feature name', max_length=100),
        ),
    ]
