# Generated by Django 3.2.13 on 2022-08-26 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0050_rename_name_links_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programs',
            old_name='category',
            new_name='vehicle',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='course',
            new_name='vehicle',
        ),
        migrations.RemoveField(
            model_name='managevehicles',
            name='category',
        ),
    ]
