# Generated by Django 2.1.12 on 2019-10-06 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20191001_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
