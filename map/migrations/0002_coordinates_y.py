# Generated by Django 2.2.16 on 2021-01-21 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinates',
            name='y',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
