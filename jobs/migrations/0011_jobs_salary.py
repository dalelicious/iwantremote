# Generated by Django 2.2.4 on 2019-10-04 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_jobs_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='salary',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
