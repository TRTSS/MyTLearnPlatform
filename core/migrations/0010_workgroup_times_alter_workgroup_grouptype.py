# Generated by Django 4.2.1 on 2023-05-08 11:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_workgroup_grouptype'),
    ]

    operations = [
        migrations.AddField(
            model_name='workgroup',
            name='times',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(null=True), null=True, size=2), blank=True, null=True, size=7),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='groupType',
            field=models.CharField(choices=[('Групповые занятия', 'Групповые занятия'), ('Индивидуальные занятия', 'Индивидуальные занятия')], default=('Групповые занятия', 'Групповые занятия'), max_length=100),
        ),
    ]
