# Generated by Django 3.2.13 on 2022-07-31 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.TextField(max_length=34)),
                ('descripton', models.TextField(max_length=34)),
                ('name', models.TextField(max_length=34)),
            ],
        ),
    ]
