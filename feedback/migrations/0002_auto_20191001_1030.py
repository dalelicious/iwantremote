# Generated by Django 2.1.12 on 2019-10-01 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='email',
            new_name='name',
        ),
    ]
