# Generated by Django 3.0.6 on 2020-05-16 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('abstract', models.CharField(blank=True, max_length=500)),
                ('authors', models.CharField(max_length=200)),
                ('journal', models.CharField(max_length=80)),
                ('date_published', models.DateField(blank=True)),
                ('doi', models.CharField(blank=True, max_length=32)),
                ('pdflink', models.CharField(blank=True, max_length=80)),
                ('rating', models.FloatField(default=0)),
                ('num_ratings', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('user', models.CharField(max_length=50)),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papers.Paper')),
            ],
        ),
    ]
