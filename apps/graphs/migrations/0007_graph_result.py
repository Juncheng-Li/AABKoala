# Generated by Django 3.1 on 2020-09-14 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0006_graph'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='result',
            field=models.ManyToManyField(to='graphs.Result'),
        ),
    ]
