# Generated by Django 3.2.13 on 2022-07-31 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0007_alter_students_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='age',
            field=models.IntegerField(max_length=34),
        ),
    ]
