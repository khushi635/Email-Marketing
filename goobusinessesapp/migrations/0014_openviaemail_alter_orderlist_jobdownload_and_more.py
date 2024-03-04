# Generated by Django 4.1.5 on 2023-02-15 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goobusinessesapp', '0013_orderlist_jobdownload'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenViaEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('openType', models.CharField(max_length=100)),
                ('openNo', models.IntegerField()),
                ('opnmessage', models.CharField(max_length=120)),
                ('lastTime', models.TimeField(auto_now=True)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='jobDownload',
            field=models.FileField(blank=True, null=True, upload_to='CompleteJobDBFolder'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='totalOrder',
            field=models.IntegerField(default=0),
        ),
    ]
