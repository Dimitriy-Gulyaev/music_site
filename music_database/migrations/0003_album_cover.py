# Generated by Django 3.0.4 on 2020-07-15 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_database', '0002_album_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
