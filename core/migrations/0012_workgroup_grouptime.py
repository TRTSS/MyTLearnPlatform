# Generated by Django 4.2.1 on 2023-05-08 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_workgroup_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='workgroup',
            name='groupTime',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
