# Generated by Django 2.0.2 on 2018-02-11 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0004_auto_20180210_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolattendance',
            name='degree_earned_year',
            field=models.DateField(null=True),
        ),
    ]
