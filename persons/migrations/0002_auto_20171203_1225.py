# Generated by Django 2.0 on 2017-12-03 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='birth_date',
            new_name='birthdate',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='last_name',
            new_name='lastname',
        ),
    ]