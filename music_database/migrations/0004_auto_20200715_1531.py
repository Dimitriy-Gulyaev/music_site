# Generated by Django 3.0.4 on 2020-07-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_database', '0003_album_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='origin',
            field=models.CharField(blank=True, choices=[('STUDIO', 'studio'), ('LIVE', 'live'), ('COMPILATION', 'compilation')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='album_covers/'),
        ),
    ]