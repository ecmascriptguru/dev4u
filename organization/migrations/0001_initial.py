# Generated by Django 2.1 on 2018-08-13 18:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 8, 13, 18, 2, 13, 659574, tzinfo=utc), verbose_name='created at')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2018, 8, 13, 18, 2, 13, 659574, tzinfo=utc), verbose_name='updated at')),
            ],
        ),
    ]
