# Generated by Django 3.2.13 on 2022-08-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0025_auto_20220809_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignments',
            name='students',
        ),
        migrations.AddField(
            model_name='assignments',
            name='student',
            field=models.CharField(default='Ali', max_length=34),
            preserve_default=False,
        ),
    ]
