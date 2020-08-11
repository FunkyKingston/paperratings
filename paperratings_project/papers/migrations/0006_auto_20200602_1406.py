# Generated by Django 3.0.6 on 2020-06-02 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('papers', '0005_auto_20200601_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='users',
            field=models.ManyToManyField(blank=True, through='papers.UserSavedPaper', to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='usersavedpaper',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]