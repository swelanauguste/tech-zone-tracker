# Generated by Django 3.2.7 on 2021-11-23 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zones', '0002_agency_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='zone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='zones.zone'),
        ),
    ]
