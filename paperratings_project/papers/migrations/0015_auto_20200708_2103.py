# Generated by Django 3.0.6 on 2020-07-08 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0014_auto_20200629_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='saved_by_users',
        ),
        migrations.DeleteModel(
            name='UserSavedPaper',
        ),
    ]