# Generated by Django 3.2.13 on 2022-08-09 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0034_alter_submitassignment_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='submitAssignment',
        ),
    ]