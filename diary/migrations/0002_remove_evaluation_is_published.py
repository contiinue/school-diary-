# Generated by Django 4.1 on 2022-10-19 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='is_published',
        ),
    ]
