# Generated by Django 3.0.6 on 2020-06-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0004_auto_20200601_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='users',
            field=models.ManyToManyField(blank=True, through='papers.UserSavedPaper', to='papers.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='papers',
            field=models.ManyToManyField(blank=True, through='papers.UserSavedPaper', to='papers.Paper'),
        ),
    ]
