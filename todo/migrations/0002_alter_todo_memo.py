# Generated by Django 5.1.3 on 2024-11-14 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='memo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
