# Generated by Django 5.0.1 on 2024-04-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0002_remove_plan_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planprice',
            name='currency',
            field=models.CharField(choices=[('INR', 'INR'), ('USD', 'USD')], max_length=10),
        ),
    ]
