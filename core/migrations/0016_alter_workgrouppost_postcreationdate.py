# Generated by Django 4.2.1 on 2023-05-09 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_workgroup_groupposts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workgrouppost',
            name='postCreationDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]