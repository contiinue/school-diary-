# Generated by Django 4.1 on 2022-11-07 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_rename_book_bookwithclass_time_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookwithclass',
            name='time_table',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='diary.schooltimetable'),
        ),
    ]
