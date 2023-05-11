# Generated by Django 4.2.1 on 2023-05-06 22:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_workgroup_lessondays'),
    ]

    operations = [
        migrations.AddField(
            model_name='workgroup',
            name='groupDays',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('ПН', 'Понедельник'), ('ВТ', 'Вторник'), ('СР', 'Среда'), ('ЧТ', 'Четверг'), ('ПТ', 'Пятница'), ('СБ', 'Суббота'), ('ВС', 'Воскресенье')], max_length=20), blank=True, default=None, size=None),
        ),
    ]