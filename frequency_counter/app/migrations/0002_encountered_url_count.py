# Generated by Django 3.1.3 on 2020-11-14 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='encountered_url',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
