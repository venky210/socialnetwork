# Generated by Django 5.0.3 on 2024-05-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_selectedtime_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
