# Generated by Django 3.0.4 on 2020-07-16 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_database', '0012_auto_20200716_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='release',
            name='charts',
        ),
        migrations.AlterField(
            model_name='release',
            name='year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Chart',
        ),
    ]
