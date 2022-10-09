# Generated by Django 3.2.13 on 2022-08-23 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0043_managevehicles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('number', models.IntegerField()),
                ('experience', models.CharField(max_length=50)),
                ('sallary', models.IntegerField()),
            ],
        ),
    ]