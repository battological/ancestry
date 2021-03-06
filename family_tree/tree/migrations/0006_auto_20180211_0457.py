# Generated by Django 2.0.2 on 2018-02-11 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0005_schoolattendance_degree_earned_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='other_notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='marriage',
            name='spouse_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='spouse2', to='tree.Person', verbose_name='Spouse'),
        ),
    ]
