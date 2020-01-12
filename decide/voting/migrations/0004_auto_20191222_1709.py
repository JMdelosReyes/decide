# Generated by Django 2.0 on 2019-12-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20180605_0842'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticalParty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Pon el nombre del partido', max_length=200, verbose_name='Name')),
                ('acronym', models.CharField(max_length=10, verbose_name='Acronym')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('headquarters', models.CharField(max_length=200, verbose_name='Headquarters')),
                ('image', models.CharField(blank=True, max_length=500, null=True, verbose_name='Image')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='politicalparty',
            unique_together={('name', 'acronym')},
        ),
    ]
