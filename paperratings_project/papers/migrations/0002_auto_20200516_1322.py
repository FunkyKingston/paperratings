# Generated by Django 3.0.6 on 2020-05-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
