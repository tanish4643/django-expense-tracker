# Generated by Django 4.2.20 on 2025-04-05 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_remove_budget_end_date_remove_budget_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='category',
            field=models.TextField(default='food'),
        ),
        migrations.AddField(
            model_name='budget',
            name='month',
            field=models.TextField(default='Apr'),
        ),
    ]
