# Generated by Django 3.0.6 on 2020-07-08 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0016_auto_20200708_2109'),
        ('accounts', '0006_auto_20200708_2016'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
