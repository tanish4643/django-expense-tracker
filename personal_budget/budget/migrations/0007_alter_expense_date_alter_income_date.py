# Generated by Django 5.2 on 2025-04-06 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0006_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
