# Generated by Django 3.1 on 2020-09-19 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('AuditID', models.CharField(max_length=45)),
                ('RevisionNumber', models.CharField(max_length=45, null=True)),
                ('FacilityName', models.CharField(max_length=100)),
                ('FacilityID', models.CharField(max_length=45)),
                ('Auditor1', models.CharField(max_length=45)),
                ('Auditor2', models.CharField(max_length=45, null=True)),
                ('Auditor3', models.CharField(max_length=45, null=True)),
                ('AuditDate', models.DateField()),
                ('RepDate', models.CharField(max_length=45)),
                ('LinacModel', models.CharField(max_length=45)),
                ('LinacManufacturer', models.CharField(max_length=45)),
                ('PlanningSystemManufacturer', models.CharField(max_length=45)),
                ('tps', models.CharField(max_length=45)),
                ('Algorithm', models.CharField(max_length=45)),
                ('kqFac', models.CharField(max_length=10)),
                ('ACDS', models.CharField(max_length=10)),
                ('Phantom', models.CharField(max_length=45, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='TPR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('energy_6', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('energy_10', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('energy_15', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('energy_18', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('energy_6FFF', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('energy_10FFF', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TPR', to='graphs.result')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Reading_101106', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_110106', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_205106', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_208106', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_205206', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_208206', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_205306', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_208306', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_303106', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_305106', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_403106', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_405106', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_103110', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_110110', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_303110', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_305110', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_403110', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_405110', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_103115', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_110115', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_303115', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_305115', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_403115', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_405115', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_103118', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_110118', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_303118', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_305118', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_403118', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_405118', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_101105', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_110105', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_303105', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_305105', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_103109', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_110109', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_303109', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('Reading_305109', models.DecimalField(decimal_places=5, max_digits=5, null=True)),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reading', to='graphs.result')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Misdelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Misdelivery_101106', models.SmallIntegerField(null=True)),
                ('Misdelivery_110106', models.SmallIntegerField(null=True)),
                ('Misdelivery_205106', models.SmallIntegerField(null=True)),
                ('Misdelivery_208106', models.SmallIntegerField(null=True)),
                ('Misdelivery_205206', models.SmallIntegerField(null=True)),
                ('Misdelivery_208206', models.SmallIntegerField(null=True)),
                ('Misdelivery_205306', models.SmallIntegerField(null=True)),
                ('Misdelivery_208306', models.SmallIntegerField(null=True)),
                ('Misdelivery_303106', models.SmallIntegerField(null=True)),
                ('Misdelivery_305106', models.SmallIntegerField(null=True)),
                ('Misdelivery_403106', models.SmallIntegerField(null=True)),
                ('Misdelivery_405106', models.SmallIntegerField(null=True)),
                ('Misdelivery_103110', models.SmallIntegerField(null=True)),
                ('Misdelivery_110110', models.SmallIntegerField(null=True)),
                ('Misdelivery_303110', models.SmallIntegerField(null=True)),
                ('Misdelivery_305110', models.SmallIntegerField(null=True)),
                ('Misdelivery_403110', models.SmallIntegerField(null=True)),
                ('Misdelivery_405110', models.SmallIntegerField(null=True)),
                ('Misdelivery_103115', models.SmallIntegerField(null=True)),
                ('Misdelivery_110115', models.SmallIntegerField(null=True)),
                ('Misdelivery_303115', models.SmallIntegerField(null=True)),
                ('Misdelivery_305115', models.SmallIntegerField(null=True)),
                ('Misdelivery_403115', models.SmallIntegerField(null=True)),
                ('Misdelivery_405115', models.SmallIntegerField(null=True)),
                ('Misdelivery_103118', models.SmallIntegerField(null=True)),
                ('Misdelivery_110118', models.SmallIntegerField(null=True)),
                ('Misdelivery_303118', models.SmallIntegerField(null=True)),
                ('Misdelivery_305118', models.SmallIntegerField(null=True)),
                ('Misdelivery_403118', models.SmallIntegerField(null=True)),
                ('Misdelivery_405118', models.SmallIntegerField(null=True)),
                ('Misdelivery_101105', models.SmallIntegerField(null=True)),
                ('Misdelivery_110105', models.SmallIntegerField(null=True)),
                ('Misdelivery_303105', models.SmallIntegerField(null=True)),
                ('Misdelivery_305105', models.SmallIntegerField(null=True)),
                ('Misdelivery_103109', models.SmallIntegerField(null=True)),
                ('Misdelivery_110109', models.SmallIntegerField(null=True)),
                ('Misdelivery_303109', models.SmallIntegerField(null=True)),
                ('Misdelivery_305109', models.SmallIntegerField(null=True)),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Misdelivery', to='graphs.result')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=250)),
                ('result', models.ManyToManyField(to='graphs.Result')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='FacilityOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('energy_6', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('energy_10', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('energy_15', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('energy_18', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('energy_6FFF', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('energy_10FFF', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facilityOutput', to='graphs.result')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
