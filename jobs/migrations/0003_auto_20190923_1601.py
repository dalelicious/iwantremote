# Generated by Django 2.1.12 on 2019-09-23 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190921_1242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='apply_link',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='jobs',
            old_name='job_description',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='jobs',
            old_name='job_title',
            new_name='title',
        ),
    ]
