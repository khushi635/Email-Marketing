# Generated by Django 4.1.5 on 2023-02-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goobusinessesapp', '0012_extraimagedb_delete_extraimageorfiledb'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='jobDownload',
            field=models.FileField(blank=True, null=True, upload_to='CompleteDBFolder'),
        ),
    ]
