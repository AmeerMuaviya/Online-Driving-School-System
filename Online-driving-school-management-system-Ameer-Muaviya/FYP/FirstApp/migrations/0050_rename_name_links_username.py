# Generated by Django 3.2.13 on 2022-08-24 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0049_links'),
    ]

    operations = [
        migrations.RenameField(
            model_name='links',
            old_name='name',
            new_name='username',
        ),
    ]
