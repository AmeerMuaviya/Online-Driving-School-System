# Generated by Django 3.2.13 on 2022-08-09 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0033_submitassignment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitassignment',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
