# Generated by Django 2.1.12 on 2019-11-26 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_auto_20191126_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='headquarters',
            field=models.CharField(max_length=100, null=True),
        ),
    ]