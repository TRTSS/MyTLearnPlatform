# Generated by Django 4.2.1 on 2023-05-09 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_workgrouppost'),
    ]

    operations = [
        migrations.AddField(
            model_name='workgroup',
            name='groupPosts',
            field=models.ManyToManyField(related_name='group_posts', to='core.workgrouppost'),
        ),
    ]