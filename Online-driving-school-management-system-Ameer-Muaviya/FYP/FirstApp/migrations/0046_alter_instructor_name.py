# Generated by Django 3.2.13 on 2022-08-23 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0045_alter_instructor_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
