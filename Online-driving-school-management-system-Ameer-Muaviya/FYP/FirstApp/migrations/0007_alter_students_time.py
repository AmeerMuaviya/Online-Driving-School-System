# Generated by Django 3.2.13 on 2022-07-31 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0006_students_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='time',
            field=models.TextField(default='', max_length=11),
        ),
    ]