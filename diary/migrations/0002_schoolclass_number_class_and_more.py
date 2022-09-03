# Generated by Django 4.1 on 2022-08-29 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolclass',
            name='number_class',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='homeworkmodel',
            name='date_end_of_homework',
            field=models.DateField(null=True, verbose_name='До какого числа домашнее задание актуально'),
        ),
        migrations.AlterField(
            model_name='homeworkmodel',
            name='home_work',
            field=models.CharField(max_length=400, verbose_name='Домашнее задание'),
        ),
        migrations.AlterField(
            model_name='homeworkmodel',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.books', verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='homeworkmodel',
            name='student_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.schoolclass', verbose_name='Класс'),
        ),
    ]
