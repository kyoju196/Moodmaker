# Generated by Django 2.2.7 on 2020-06-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='information_board',
            fields=[
                ('no', models.AutoField(db_column='No', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='TITLE', max_length=200)),
                ('content', models.CharField(db_column='CONTENT', max_length=1000)),
            ],
        ),
    ]