# Generated by Django 3.2.13 on 2022-08-09 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0032_remove_submitassignment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitassignment',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
