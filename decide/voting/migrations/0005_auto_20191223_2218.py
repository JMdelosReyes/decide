# Generated by Django 2.0 on 2019-12-23 22:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_auto_20191222_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politicalparty',
            name='headquarters',
            field=models.CharField(help_text='The direction of the headquarters', max_length=200, verbose_name='Headquarters'),
        ),
        migrations.AlterField(
            model_name='politicalparty',
            name='image',
            field=models.CharField(blank=True, help_text='Must be a link', max_length=500, null=True, validators=[django.core.validators.URLValidator()], verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='politicalparty',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
    ]
