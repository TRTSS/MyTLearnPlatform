# Generated by Django 4.2.1 on 2023-05-07 09:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_alter_workgroup_groupname'),
    ]

    operations = [
        migrations.AddField(
            model_name='workgroup',
            name='groupStudents',
            field=models.ManyToManyField(related_name='group_students', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='groupDays',
            field=models.ManyToManyField(related_name='group_days', to='core.workday'),
        ),
    ]
