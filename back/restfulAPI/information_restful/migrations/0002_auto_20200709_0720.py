# Generated by Django 2.2.7 on 2020-07-09 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information_restful', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='information',
            old_name='body',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='information',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]