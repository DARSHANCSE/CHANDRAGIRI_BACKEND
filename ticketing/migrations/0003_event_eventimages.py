# Generated by Django 4.2.5 on 2024-11-29 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0002_rename_count_monitoring_entrycount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventimages',
            field=models.ImageField(blank=True, null=True, upload_to='Event_images/'),
        ),
    ]
