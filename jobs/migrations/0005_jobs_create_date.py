# Generated by Django 2.1.12 on 2019-09-24 10:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_jobs_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
