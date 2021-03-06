# Generated by Django 2.0 on 2017-12-03 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20171203_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birth_certificate',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='birth_place',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='birth_source_doc',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='death_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='death_place',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='death_source_doc',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='first_names',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
