# Generated by Django 3.2.13 on 2022-07-31 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0003_auto_20220731_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='gender',
            field=models.TextField(default='', max_length=10),
        ),
    ]