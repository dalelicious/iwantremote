# Generated by Django 2.2.4 on 2019-10-04 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20191001_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='job_title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
