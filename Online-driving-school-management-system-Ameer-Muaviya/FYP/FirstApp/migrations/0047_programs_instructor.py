# Generated by Django 3.2.13 on 2022-08-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0046_alter_instructor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='programs',
            name='instructor',
            field=models.CharField(default='ali', max_length=25),
            preserve_default=False,
        ),
    ]
