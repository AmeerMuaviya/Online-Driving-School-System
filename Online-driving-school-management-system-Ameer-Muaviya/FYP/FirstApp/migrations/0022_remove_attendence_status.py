# Generated by Django 3.2.13 on 2022-08-09 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0021_notifications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendence',
            name='status',
        ),
    ]
