# Generated by Django 3.1 on 2020-10-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0006_auto_20201004_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='FacilityID',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='RepDate',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
