# Generated by Django 3.2.13 on 2022-08-09 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0022_remove_attendence_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='status',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
