# Generated by Django 4.2.1 on 2023-05-08 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_workgroup_times_alter_workgroup_grouptype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workgroup',
            name='times',
        ),
    ]
