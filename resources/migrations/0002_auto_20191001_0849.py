# Generated by Django 2.1.12 on 2019-10-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='content',
            field=models.CharField(max_length=200, null=True),
        ),
    ]