# Generated by Django 3.2.13 on 2022-08-07 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0018_alter_attendence_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(max_length=500)),
                ('category', models.CharField(max_length=25)),
            ],
        ),
    ]
