# Generated by Django 4.2.1 on 2023-05-06 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_workday_remove_workgroup_groupdays_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workgroup',
            name='groupName',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
