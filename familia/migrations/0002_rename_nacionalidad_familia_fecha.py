# Generated by Django 4.0.5 on 2022-06-26 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familia',
            old_name='nacionalidad',
            new_name='fecha',
        ),
    ]