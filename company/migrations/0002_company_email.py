# Generated by Django 2.1.12 on 2019-09-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
