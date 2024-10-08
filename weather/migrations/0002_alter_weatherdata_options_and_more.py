# Generated by Django 5.1 on 2024-08-21 17:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weatherdata',
            options={'ordering': ['-timestamp']},
        ),
        migrations.RemoveField(
            model_name='weatherdata',
            name='weather_condition',
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='humidity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='temperature',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
