# Generated by Django 3.2.13 on 2022-08-11 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0037_auto_20220811_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='time',
            field=models.ImageField(upload_to='profile'),
        ),
    ]